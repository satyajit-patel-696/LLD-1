#here i will use the base model to create a simple class and then i will use the property decorator to create a getter and setter method for the private variable and also i will use the multiple inheritance to create a class that inherits from two classes and then i will use the method resolution order to see the order of the classes in the inheritance hierarchy
from pydantic import BaseModel, field_validator
class User(BaseModel):
    name:str
    age:int
    @field_validator('age')
    def validate_age(cls, value):
        if value < 0:
            raise ValueError("Age must be a positive integer")
        return value
#base model is a class that is used to create a model that can be used to validate the data and also to create a model that 
# can be used to serialize and deserialize the data and also to create a model