# class Student:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age

#     def display(self):
#         print(f"Name: {self.__name}, Age: {self.age}")
# student1 = Student("Alice", 20)
# student1.display()  
# print(student1._Student__name)



class A:
    def show(self):
        print("This is class A")
class B:
    def show(self):
        print("This is class B")
class C(A,B):
    pass
c = C()
c.show()  # Output: This is class A
print(C.__mro__) 
print(C.mro())
B.show(c) # Output: (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)