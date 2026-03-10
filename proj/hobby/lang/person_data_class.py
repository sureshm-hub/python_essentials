from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str
    height: float = 0.0 # Default value

# By default, Python dataclasses are mutable

# Instantiating the class
person1 = Person("Alice", 30, "alice@example.com", height=1.75)
person2 = Person("Bob", 25, "bob@example.com")
person3 = Person("Alice", 30, "alice@example.com", height=1.75)

# Automatically generated methods in action:

# __repr__ (printing the object)
print(f"Representation: {person1}")
# Output: Representation: Person(name='Alice', age=30, email='alice@example.com', height=1.75)

# __eq__ (comparing objects by value)
print(f"Equality check: {person1 == person3}")
# Output: Equality check: True

print(f"Equality check: {person1 == person2}")
# Output: Equality check: False