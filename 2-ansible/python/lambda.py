import re

a = [4, 3, 7, 2]
print(sorted(a))
b = ['!abc', '~ABC', 'def', 'DEF']
print(sorted(b))
c = [('nick', 100), ('nick', 0), ('jose', 80)]
print(sorted(c))
# d = [['nick', 100], ['nick', 0], ['jose', 80]]
# print(sorted(d))

# sequences like list,tuple are compared element-wise by default.
# all ways of comparing boil down to how the < and == operators behave (and therefore, >, >=, <=, !=)

# functions like min, max, sorted accept a keyword-only parameter "key".
# that parameter's value must be a function. that function is applied to
# each thing that is compared, so that only the result of that function is what's actually compared.


# def get_second_value(x):
#     return x[1]

# # c = [(x[1], x[0]) for x in c]
# print(sorted(c, key=get_second_value))

# among python's "functional programming" influenced features -
#  we can treat functions as just another kind of value that could be a function parameter, part of a list, or anything
#  a function is very different from a function's return value

# lambda expression is a syntax allowing the creation of functions inline as an expression
# it's like a "function literal"
# after the keyword "lambda", you define the parameter.
# after the colon, you put an expression that will be the return value.

print(sorted(c, key=(lambda x: x[1])))

print(sorted(b, key=(lambda x: x.lower())))
print(sorted(b, key=(lambda x: re.sub('[^a-z]', '', x.lower()))))
print(sorted(b, key=(lambda x: [c.lower() for c in x if c.isalpha()])))

print(list(map(lambda x: len(x), b)))
print(list(map(len, b))) # ^equivalent

g = ['123', '1565']
# [int(g[0]), int(g[1])]
[int(x) for x in g]
list(map(int, g)) # ^ equivalent
list(int(x) for x in g)  # ^ equivalent
# "map" and "filter" do not return lists or anything else that's a "materialized" sequence
# they return an object that can yield values one by one if you were to iterate over it
#   (e.g. in a for loop.)
# this works the same as "range" objects.
# aka "lazy evaluation" instead of "eager evaluation"
list(range(0, 1000))

print(list(filter(lambda x: x.endswith('3'), g)))

# one way in python to make your own lazily-evaluated sequences
# is special generator functions like this that use "yield" instead of "return":
def fib():
    a, b = 0, 1
    while True:
        yield b
        print(f'{b} from generator')
        a, b = b, a+b

for n in fib():
    print(f'{n} from loop')
    if n > 20:
        break

# another way is to write what would be a list comprehension, but use
# parentheses instead of brackets.
# "generator expression"
lazy = (int(x) for x in g)
print(*lazy)
print(123, 123)

# the nicest way in python to "get the first element of a sequence matching a condition"
# is a generator expression with the builtin function "next" that gets the next value of any iterable
sequence = [1, 3, 25, 40]
print(next(n for n in sequence if n > 20))

if any(x < 0 for x in sequence):
    print('negative')
