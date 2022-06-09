# x = input()

# if x == 'a':
#     print('a')

# print('done')

def add(a, b):
    return a + b


# languages that have variables and multiple data types
# can take a couple different approaches.
print(add(2, 3))
print(add('asdf', 'jkl'))
print(add(add, add))

# "dynamically-typed" languages
# let you send any kind of data from one part of the
# program to another (any variable can hold any kind of data)
# and the code that operates on that data will just either
# work or break at runtime.

# statically-typed languages, instead,
# require every variable to allow only a certain type of data
# and you'll get an error "earlier" (maybe at compile-time)
# if you break those rules

# "garbage-collected" -
#  python periodically scans the program memory
#  for anything that could not possibly be accessed
# anymore by valid python code, and frees that memory
# to be reused (rather than the programmer having to
# reason about when to free it)
# this is a tradeoff of spending more computer time
# to have more human time

# python did a few versions ago learn about "type annotations"
# like above, but the runtime ignores them.
# there are only for documentation or for
# other tools to read


# programming paradigms -
    # how do we manage complexity in the program?

# the procedural way:
    # break up the work to be done hierarchically
    # into high-level and low-level tasks
    # separate any duplicated code into reusable
    #   functions/subroutines

# the object-oriented way:
    # consider what data and behavior accompany each other
    # in the logic of the work to be done.
    # example: every time we modify some data,
        # we have to check it for correctness.
    # OOP says: instead of having to remember to check the data
    # every time you modify the data -
    # encapsulate the data and the behavior in an object.
    # the ONLY WAY to modify that data will be through the object
    # and that object will define the checks that will run
    # any time you try to modify that data.
    # each object is responsible for its own data

# the functional way:
    # break up the work into small composable functions
    # each function thinks only about its input and its output.
    # we try to avoid functions having "side-effects"
    # so instead of modifying data, we try to just leave
    # the original data in place, and return a new separate version of the data for whatever result
    # we treat functions as just another kind of data like
    # numbers or strings. so we can have functions that turn
    # functions into other functions
