# collection

# lists
# mutable sequences of whatever you want
# empty list
x = []
# creating list with initial contents
#    0  1  2  3  4  5  6  7
x = [1, 2, 3, 7, 3, 1, 7, 4]
# create list from another sequence
x2 = list('abc')
# index into the list with numbers
# the first element
x[0]
# slice the list to get sublists (copy part of the list into a new list)
y = x[1:] # everything in the list except the first element
# with slices: [start:stop:step], defaults are 0, len(sequence), 1 respectively
z = x[:1] # everything in the list up to the second element
# x == x[:n] + x[n:] # how we could splitting list in two
x[2:5]
x[2:-3]
z = [
    [1, 2],
    [3, 4]
]
if 0 not in x:
    print('zero wasn\'t found')
# https://docs.python.org/3/library/stdtypes.html#common-sequence-operations

# enumerate is a builtin function that turns a sequence of things
# into a sequence of tuples containing the thing and the index of the thing
for index, element in enumerate(x):
    if element < index:
        print(element)


# tuples
# a tuple is an immutable sequence
# constructed with parentheses instead of brackets
data = ('asdf', 10, 1234)
# many of the things we can do with lists we can also do with tuples
data = 'fdsa', data[1], data[2]

# we use lists when we have a sequence of values that are
# usually the same kind of thing
# we use tuples when we have a handful of pieces of data
#   that belong together
projects = [
    ('nick', 'scrabble game', 'https://github.com/etc', 0, ['eli', 'timothy']),
    ('nick', 'scrabble game', 'https://github.com/etc', 0, [])
]

projects[0][0] # the name of the owner of the first project

# assigns several variables to each element of a tuple
# destructuring/unpacking
name, app, url, completion, _ = projects[0]
name, app, url, completion = 'nick', 'scrabble game', 'https://github.com/etc', 0
_, app, *_ = projects[1]

proj0, proj1 = projects

# strings are sequences of strings
for i, c in enumerate('asdf'):
    # f-strings
    print(f'{i + 1}: {c}')


# set
# a set is a unordered mutable group of things
# there is no concept of duplicates in a set, if you try to add them, they are ignored
# it's that kind of set that can do "union", "intersection", "difference"
# we use a set instead of a list when:
# - we don't care about the order of the items, and/or
# - we want checking for membership of the set to be fast
# empty set
x = set()
# set with initial values
x = { 1, 3, 5, 7 }
#set made out of some other sequence
x = set('abcdef')

word = 'apple'
# how many unique letters are in that word?
print(len(set(word)))
# show all letters that are not in that word
print(set('abcdefghijklmnopqrstuvwxyz') - set(word))
# in order
print(''.join(sorted(set('abcdefghijklmnopqrstuvwxyz') - set(word))))
valid_users = {'a', 'b', 'c', 'd', 'e'}
# add, remove
valid_users.add('f')

user_input = 'z'
if user_input in valid_users:
    print('login')
else:
    print('invalid user')

# dicts (dictionaries)
# collection of key-value pairs
# dicts are like sets in that it is fast to find a value by its key
#   even if the dict is large
# empty dict
x = {}
# dict with initial contents
x = {
    'key1': 'value1',
    'key2': 123,
    12: 'abc'
}
# access values by their key (throws a KeyError if not found)
y = x[12]
y = x['key2']
# access values by their key (return None if not found)
y = x.get(12)
y = x.get('key2')
# modify existing key-value pairs or add new ones
x['key3'] = 123
x['key3'] = 124

# iterate over the keys, the values, or both:
for key in x:
    pass
for value in x.values():
    pass
for key, value in x.items():
    pass

# when to use dicts:
# 1. any time we want to "look up" some data based on some other data
# 2. like how tuples can encapsulate related data about one thing in one unit,
    #  dicts can do that too

projects = {
    'scrabble game': ('nick', 'https://github.com/etc', 0, ['eli', 'timothy']),
    'scrabble game 2': ('nick', 'https://github.com/etc', 0, [])
}

projects = {
    'scrabble game': {
        'owner': 'nick',
        'url': 'https://github.com/etc',
        'completion': 0,
        'collaborators': ['eli', 'timothy']
    }
}

projects['scrabble game']['collaborators'] # the list of collaborators

# projects['scrabble game']['url']
if 'scrabble game' in projects and 'url' in projects['scrabble game']:
    url = projects['scrabble game']['url']
else:
    print('data in unrecognized format')

# dicts do keep track of their insertion order, and iteration over them
#   will reflect that order (unlike sets)

projects.get('scrabble game').get('url')

data = [ 2, 5, 3, 8 ]
# comprehensions

collection = []  # any collection not just list
for x in data:
    for y in data:
        if x != 0:
            collection.append(x * y)

# list comprehension
collection2 = [x ** 2 for x in data]
collection2 = [x * y for x in data for y in data if x != 0]

# set comprehension
set_comp = {x ** 2 for x in data}

# dict comprehension
nums_to_squares = {x: x ** 2 for x in data}
squares_to_nums = {x ** 2: x for x in data}

# in python, every file is a "module"
   # the name of that module is the filename minus the .py
# one way to execute a module
