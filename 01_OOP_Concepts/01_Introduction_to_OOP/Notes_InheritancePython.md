### **Inheritance in Python**

Inheritance is a mechanism in object-oriented programming that allows a class (called the **child class** or **derived class**) to inherit properties and methods from another class (called the **parent class** or **base class**). It enables code reuse and the creation of hierarchical relationships between classes.

---

### **Key Features of Inheritance:**
1. **Code Reusability**: Allows child classes to reuse methods and properties of the parent class.
2. **Method Overriding**: Child classes can provide their own implementation of methods from the parent class.
3. **Extensibility**: Child classes can add new properties or methods in addition to inherited ones.
4. **Multiple Levels**: Supports single, multiple, and multi-level inheritance.

---

### **Types of Inheritance in Python:**

1. **Single Inheritance**: A child class inherits from one parent class.
2. **Multiple Inheritance**: A child class inherits from multiple parent classes.
3. **Multi-level Inheritance**: A class inherits from a class, and another class inherits from it.
4. **Hierarchical Inheritance**: Multiple child classes inherit from a single parent class.
5. **Hybrid Inheritance**: A combination of two or more types of inheritance.

---

### **Examples of Inheritance**

#### **1. Single Inheritance**
```python
class Parent:
    def show(self):
        print("This is a method in the Parent class.")

class Child(Parent):
    def display(self):
        print("This is a method in the Child class.")

# Create an instance of the Child class
obj = Child()
obj.show()     # Accessing the parent class method
obj.display()  # Accessing the child class method
```

---

#### **2. Multiple Inheritance**
```python
class Parent1:
    def method1(self):
        print("This is method1 from Parent1.")

class Parent2:
    def method2(self):
        print("This is method2 from Parent2.")

class Child(Parent1, Parent2):
    def method3(self):
        print("This is method3 from Child.")

# Create an instance of the Child class
obj = Child()
obj.method1()  # From Parent1
obj.method2()  # From Parent2
obj.method3()  # From Child
```

---

#### **3. Multi-level Inheritance**
```python
class Grandparent:
    def method1(self):
        print("This is a method from the Grandparent class.")

class Parent(Grandparent):
    def method2(self):
        print("This is a method from the Parent class.")

class Child(Parent):
    def method3(self):
        print("This is a method from the Child class.")

# Create an instance of the Child class
obj = Child()
obj.method1()  # From Grandparent
obj.method2()  # From Parent
obj.method3()  # From Child
```

---

#### **4. Hierarchical Inheritance**
```python
class Parent:
    def method1(self):
        print("This is a method in the Parent class.")

class Child1(Parent):
    def method2(self):
        print("This is a method in the Child1 class.")

class Child2(Parent):
    def method3(self):
        print("This is a method in the Child2 class.")

# Instances of Child1 and Child2
obj1 = Child1()
obj2 = Child2()

obj1.method1()  # From Parent
obj1.method2()  # From Child1

obj2.method1()  # From Parent
obj2.method3()  # From Child2
```

---

#### **5. Hybrid Inheritance**
```python
class Base:
    def method1(self):
        print("This is a method in the Base class.")

class Child1(Base):
    def method2(self):
        print("This is a method in the Child1 class.")

class Child2(Base):
    def method3(self):
        print("This is a method in the Child2 class.")

class GrandChild(Child1, Child2):
    def method4(self):
        print("This is a method in the GrandChild class.")

# Create an instance of GrandChild
obj = GrandChild()
obj.method1()  # From Base
obj.method2()  # From Child1
obj.method3()  # From Child2
obj.method4()  # From GrandChild
```

---

### **Method Overriding**
When a child class provides its own implementation of a method defined in the parent class.

```python
class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self):  # Overriding the Parent method
        print("Hello from Child!")

obj = Child()
obj.greet()  # Output: Hello from Child!
```

---

### **The `super()` Function**
The `super()` function is used to call a method or constructor from the parent class.

```python
class Parent:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Parent Name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calling Parent's constructor
        self.age = age

    def show(self):
        super().show()  # Calling Parent's method
        print(f"Child Age: {self.age}")

obj = Child("John", 12)
obj.show()
```

---

### **Key Benefits of Inheritance**
1. **Code Reusability**: Eliminates code duplication.
2. **Improved Code Structure**: Helps in organizing code in a hierarchical manner.
3. **Extensibility**: Makes it easier to extend functionality.
