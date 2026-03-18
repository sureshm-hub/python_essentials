from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql.window import Window, WindowSpec
from pyspark.storagelevel import StorageLevel

spark = (SparkSession.builder.appName("pyspark_basic")
         .config("spark.sql.execution.arrow.pyspark.enabled", "true")
         .config("spark.sql.execution.pyspark.udf.faulthandler.enabled", "true")
         .config("spark.python.worker.faulthandler.enabled", "true") # optional:
         .getOrCreate())

data = [
    (1, 2, "Alice", 25),
    (2, 2, "Bob", 30),
    (3, 1, "Charlie", 35),
    (4, 3, "David", 40),
    (5,5, "Eve", 25)
]

# schema = StructType([
#     StructField("id", IntegerType(), True),
#     StructField("dept_id", IntegerType(), True),
#     StructField("name", StringType(), True),
#     StructField("age", IntegerType(), True)
# ])
# df = spark.createDataFrame(data, schema)

cols = ["id","dept_id","name","age"]
df = spark.createDataFrame(data, cols)

dept = [
    (1, "IT"),
    (2, "HR"),
    (3, "Finance")
]

dept_schema = StructType([
    StructField("dept_id", IntegerType(), True),
    StructField("dept_name", StringType(), True)
])

dept = spark.createDataFrame(dept, dept_schema)

df.show()
# select filter
df.select("name").filter(F.lower(F.col("name")).startswith("a")).show()

# group by
df.groupBy(F.col("age")).count().show()

# join
df.join(dept, df.dept_id == dept.dept_id, "outer").show()

# window
spec = Window.partitionBy("dept_id").orderBy("age")
df.withColumn("rank", F.rank().over(spec)).show()

# persist vs cache
df.cache()
df.persist(StorageLevel.DISK_ONLY)
df.unpersist()

#broadcast join
denorm = df.join(F.broadcast(dept), df.dept_id == dept.dept_id, "outer").drop(dept.dept_id)

#repartition
denorm_partition = denorm.repartition(2, "name", "dept_name")

#coalesce - prod bottleneck when coalescing into 1
denorm_coalsce = denorm_partition.coalesce(1)
denorm_coalsce.write.mode("overwrite").parquet("C:/Users/sures/IdeaProjects/PythonEssentials/out/parquet")
denorm_coalsce.write.mode("overwrite").csv("C:/Users/sures/IdeaProjects/PythonEssentials/out/csv")

# Define & Apply pandas
import pandas as pd
from pyspark.sql.functions import pandas_udf


@pandas_udf("long")
def pandas_id_plus_one(series: pd.Series) -> pd.Series:
    return series + 1

df.select(pandas_id_plus_one("id")).show()

spark.stop()