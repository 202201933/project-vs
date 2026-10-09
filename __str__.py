class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

p = Person("Alice", 30)

print(p) #내부적으로 str 호출함
print(str(p)) #직접 호출

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x},{self.y})"
    
v1 = Vector(2,3)
v2 = Vector(4,5)

print(v1 + v2)