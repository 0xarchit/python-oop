
### **1. Class Variables**
- **Definition**: Attributes that are shared across all instances of a class. They belong to the class itself and not any specific instance.
- **Scope**: Shared among all instances of the class.
- **Use Case**: Used for data or properties that are common to all objects of the class.
- **Declared**: Inside the class definition, but outside of any instance methods.

**Example**:
```python
class Car:
    wheels = 4  # Class variable, shared by all instances

    def __init__(self, brand):
        self.brand = brand  # Instance variable, unique to each instance

# Accessing the class variable
print(Car.wheels)  # Output: 4

car1 = Car("Toyota")
car2 = Car("Honda")

# Accessing the class variable through instances
print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4

# Modifying the class variable
Car.wheels = 6
print(car1.wheels)  # Output: 6
print(car2.wheels)  # Output: 6
```

---

### **2. Instance Variables**
- **Definition**: Attributes that are specific to an instance. Each instance has its own copy.
- **Scope**: Unique to each instance.
- **Use Case**: Used for data or properties that vary between instances.
- **Declared**: Inside the `__init__` method or other instance methods using `self`.

**Example**:
```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand  # Instance variable
        self.color = color  # Instance variable

car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

# Accessing instance variables
print(car1.brand)  # Output: Toyota
print(car2.color)  # Output: Blue

# Modifying instance variables
car1.color = "Green"
print(car1.color)  # Output: Green
print(car2.color)  # Output: Blue
```

---

### **Key Differences**

| **Aspect**           | **Class Variable**             | **Instance Variable**          |
|-----------------------|-------------------------------|--------------------------------|
| **Scope**             | Shared among all instances    | Specific to a single instance  |
| **Declaration**       | Outside methods, in the class | Inside methods, typically in `__init__` |
| **Access**            | Accessed via class or instance| Accessed only via instance     |
| **Modification**      | Affects all instances (if modified using the class name) | Affects only the specific instance |
| **Use Case**          | Common properties for all objects | Unique properties for each object |

---

### **Combined Example**
```python
class Car:
    wheels = 4  # Class variable

    def __init__(self, brand, color):
        self.brand = brand  # Instance variable
        self.color = color  # Instance variable

car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

# Class variable
print(Car.wheels)  # Output: 4
print(car1.wheels)  # Output: 4

# Instance variables
print(car1.brand)  # Output: Toyota
print(car2.color)  # Output: Blue
```
