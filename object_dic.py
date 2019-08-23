#import requests
#import json

class Person:
    def __init__(self, name, age,
                 city):
        self.name = name
        self.age = age
        self.city = city
    def __str__(self):
        #return f'name : {self.name}
        # age : {self.age}'
        result = ""
        for k, v in self.__dict__.items():
            result += k
            result += " : "
            result += str(v)
            result += '\n'
        return result

# moshe = Person('Moshe', 37, "Ashdod")
initParam = {'name' : 'Moshe', 'age' : '37', 'city' : 'Ashdod'}

# this needs to work
moshe = person(initParam)



