class Car:
    class_var_brand = "Generic"

    def __init__(self, model):
        self.inst_var_model = model

    def display(self):
        return f"brand: {self.class_var_brand} & model: {self.inst_var_model}"

    #Use @classmethod for alternate constructors or factory patterns or operations concerning all instances of a class
    @classmethod
    def from_string(cls, car_str):
        model = car_str.split('-')[1]
        return cls(model)

    # utility methods
    @staticmethod
    def is_valid_model(model):
        return isinstance(model, str) and len(model) > 0

#Usage:
car = Car.from_string("Generic-Tesla")
print(car.display())
print(Car.is_valid_model("Cybertruck"))