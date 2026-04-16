# class Parent1:
#     def __init__(self,name):
#         self.name = name
#         print("Parent1 constructor called")
# class Parent2:
#     def __init__(self,age):
#         self.age = age
#         print("Parent2 constructor called")

# class Child(Parent1,Parent2):
#     def __init__(self,name,age):
#         Parent1.__init__(self,name)
#         Parent2.__init__(self,age)
#         print("Child constructor called")
# child = Child("Alice", 20)
# print(f"Name: {child.name}, Age: {child.age}")

#type 2
class Parent1:
    def __init__(self,name,title):
        self.name = name
        self.title = title
        print("Parent1 constructor called")
class Parent2:
    def __init__(self,age):
        self.age = age
        print("Parent2 constructor called")
class Child(Parent1,Parent2):
    def __init__(self,name,age,title):
        super().__init__(name, title)
        # super().__init__(age)
        print("Child constructor called")
child = Child("Alice", 20, "Dr.")
print(f"Name: {child.name}, Title: {child.title}")