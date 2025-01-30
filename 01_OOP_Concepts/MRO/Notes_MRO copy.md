
### **MCQs on MRO and Inheritance**

#### **1. What does MRO stand for in Python?**
a) Method Resolution Order  
b) Method Retrieval Operation  
c) Method Reference Object  
d) Method Reusability Option  
**Answer**: a) Method Resolution Order  

---

#### **2. Which algorithm does Python use to determine MRO?**
a) Depth-First Search (DFS)  
b) Breadth-First Search (BFS)  
c) C3 Linearization  
d) Dijkstra's Algorithm  
**Answer**: c) C3 Linearization  

---

#### **3. In Python, which attribute is used to view the MRO of a class?**
a) `__mro__`  
b) `__inheritance__`  
c) `__order__`  
d) `__hierarchy__`  
**Answer**: a) `__mro__`  

---

#### **4. What is the output of the following code?**
```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
```
a) `[D, B, C, A, object]`  
b) `[D, B, A, C, object]`  
c) `[D, C, B, A, object]`  
d) `[D, A, B, C, object]`  
**Answer**: a) `[D, B, C, A, object]`  

---

#### **5. What is the purpose of the `super()` function in Python?**
a) To call a method from a sibling class  
b) To call a method from a parent class  
c) To call a method from a child class  
d) To call a method from an unrelated class  
**Answer**: b) To call a method from a parent class  

---

#### **6. What will be the output of the following code?**
```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")
        super().greet()

class C(A):
    def greet(self):
        print("Hello from C")
        super().greet()

class D(B, C):
    def greet(self):
        print("Hello from D")
        super().greet()

d = D()
d.greet()
```
a)  
```
Hello from D  
Hello from B  
Hello from C  
Hello from A  
```  
b)  
```
Hello from D  
Hello from B  
Hello from A  
```  
c)  
```
Hello from D  
Hello from C  
Hello from B  
Hello from A  
```  
d)  
```
Hello from D  
Hello from A  
```  
**Answer**: a)  
```
Hello from D  
Hello from B  
Hello from C  
Hello from A  
```  

---

#### **7. Which of the following is true about MRO in Python?**
a) MRO is only applicable to single inheritance.  
b) MRO ensures that no class is visited more than once.  
c) MRO follows a depth-first search approach.  
d) MRO is not used in Python 3.  
**Answer**: b) MRO ensures that no class is visited more than once.  

---

#### **8. What will be the output of the following code?**
```python
class X:
    pass

class Y:
    pass

class Z:
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(A, B, Z):
    pass

print(M.mro())
```
a) `[M, A, X, B, Y, Z, object]`  
b) `[M, A, B, X, Y, Z, object]`  
c) `[M, B, A, X, Y, Z, object]`  
d) `[M, A, B, Y, X, Z, object]`  
**Answer**: a) `[M, A, X, B, Y, Z, object]`  

---

#### **9. Which of the following is a valid use of `super()`?**
a) `super().__init__()`  
b) `super().method_name()`  
c) Both a and b  
d) None of the above  
**Answer**: c) Both a and b  

---

#### **10. What will happen if a class inherits from two classes that have a common parent?**
a) Python will raise a `TypeError`.  
b) Python will use the C3 Linearization algorithm to resolve the MRO.  
c) Python will randomly choose one of the parent classes.  
d) Python will ignore the common parent.  
**Answer**: b) Python will use the C3 Linearization algorithm to resolve the MRO.  

---

#### **11. What is the default base class for all classes in Python?**
a) `object`  
b) `class`  
c) `type`  
d) `base`  
**Answer**: a) `object`  

---

#### **12. What will be the output of the following code?**
```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.__mro__)
```
a) `(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)`  
b) `(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>)`  
c) `(<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)`  
d) `(<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)`  
**Answer**: a) `(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)`  

---

#### **13. Which of the following is true about multiple inheritance in Python?**
a) It is not supported in Python.  
b) It can lead to the diamond problem.  
c) It always follows a depth-first search approach.  
d) It is resolved using the BFS algorithm.  
**Answer**: b) It can lead to the diamond problem.  

---

#### **14. What is the diamond problem in inheritance?**
a) A problem where a class inherits from multiple classes with no common parent.  
b) A problem where a class inherits from multiple classes with a common parent.  
c) A problem where a class inherits from itself.  
d) A problem where a class cannot inherit from more than one class.  
**Answer**: b) A problem where a class inherits from multiple classes with a common parent.  

---

#### **15. What will be the output of the following code?**
```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    pass

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass

d = D()
d.greet()
```
a) `Hello from A`  
b) `Hello from B`  
c) `Hello from C`  
d) `Hello from D`  
**Answer**: c) `Hello from C`  

---

#### **16. Which of the following is true about the `super()` function?**
a) It can only be used in single inheritance.  
b) It can only be used in the `__init__` method.  
c) It follows the MRO to call methods.  
d) It cannot be used with multiple inheritance.  
**Answer**: c) It follows the MRO to call methods.  

---

#### **17. What will happen if a class inherits from itself?**
a) Python will raise a `TypeError`.  
b) Python will allow it and create a recursive inheritance.  
c) Python will ignore the inheritance.  
d) Python will create a new class.  
**Answer**: a) Python will raise a `TypeError`.  

---

#### **18. What is the output of the following code?**
```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.mro())
```
a) `[C, B, A, object]`  
b) `[C, A, B, object]`  
c) `[C, B, object, A]`  
d) `[C, A, object, B]`  
**Answer**: a) `[C, B, A, object]`  

---

#### **19. Which of the following is true about the `__mro__` attribute?**
a) It is a list.  
b) It is a tuple.  
c) It is a dictionary.  
d) It is a set.  
**Answer**: b) It is a tuple.  

---

#### **20. What will be the output of the following code?**
```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass

print(C.mro())
```
a) `[C, A, B, object]`  
b) `[C, B, A, object]`  
c) `[C, A, object, B]`  
d) `[C, B, object, A]`  
**Answer**: a) `[C, A, B, object]`  

---
