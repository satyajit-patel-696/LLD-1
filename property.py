#property in python used for getter and setter method and 
# also for deleting the method its useful when we want to access 
# the private variable outside the class and a
# lso we can set the value of private variable outside the class 
# and also we can delete the value of private variable outside the class
# we can also use property decorator for getter and setter method and also for deleting the method
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
    @name.getter
    def name(self):
        return self.__name.upper()

    @name.deleter
    def name(self):
        del self.__name
student1 = Student("Alice", 20)
print(student1.name)  # Output: Alice 
student1.name = "Bob"
print(student1.name)  # Output: Bob
del student1.name
# print(student1.name)  # This will raise an AttributeError since the name attribute has been deleted  