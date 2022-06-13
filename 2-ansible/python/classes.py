class InvalidPersonError(Exception): pass

class Person:
    # you don't have to "declare fields" or anything like that.
    # by default, custom objects created from classes can just get new
    # attributes assigned to them
    # in other languages, you can't tack on new instance variables (aka fields)
    # besides the ones defined by the class. you can in python

    # one thing you often do in a class is define a constructor/initializer/__init__ method.
    # "methods" are functions attached to an object or class
    # you define them indented within the class.
    # then, they can be called "on" any instance of that class, using "."
    # when you do call them that way, python "rewrites" it so that
    # the thing to the left of the dot becomes the first argument of that function. conventionally name it "self"
    def __init__(self, id_, name):
        self.id = id_
        self.name = name
        if not self.is_valid():
            raise InvalidPersonError('invalid input')

    def __str__(self):
        # return f'Person({self.id}, {self.name})'
        return f'{self.id} {self.name}'

    # call this with "person.is_valid()" - "person" will become "self"
    def is_valid(self):
        try:
            return self.id > 0 and len(self.name) > 0
        except (AttributeError, TypeError):
            return False

# basic OO idea:

# writing code, we find that some pieces of data
# are always used together
student_ids = [1, 2, 3, 4]
student_names = ['bob', 'tim', 'fred']

# rather than accidentally associating that data, let's use data structures
# intelligently to keep it organized together
student_info = [(1, 'bob'), (2, 'tim'), (3, 'fred')]
# combine data and associated behavior into one unit called an object
# encapsulation  - combining these things into one unit
#    that controls access/its own rules about that stuff

student1 = Person(1, 'bob')

print(student1)

print(f'{student1} ({student1.is_valid()})')

# __init__ is not the only special method name
# we call them "double underscore" or "dunder" methods
# they are how you override a bunch of python's default behavior.

# classes are templates for making new objects

def get_name(anything):
    return anything.name

get_name(student1)
