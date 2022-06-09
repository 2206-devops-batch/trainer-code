print('Hello world')

# python has some data types
x = 2 + 2
# "int" data type for whole numbers
# "float" data type for fractional numbers
print(x)

# "str" data type for strings and characters
#   use double quotes or single quotes (same)
x = 'hello'

print(x.upper())

# in python, data and related behavior
# are often (but not always) combined into objects -
# so the behavior can be accessed as "methods" on the data.

# we have a lot of operators familiar from many similar programming languages

x = 2 + 3 - 5 * 6 / 7

print(x)

# boolean operators "and", "or", "not"

print(x < 1 or x > 2)
print(x < 1 and x > 2)

print('abcdef'[0])  # the first character (a)
print('abcdef'[1])  # the second character (b)
print('abcdef'[-1])  # the last character (f)

# slicing
print('abcdef'[0:3])  # a substring including 0,1, and 2 (abc)

# conditionals
if 3 < 4:
    print('three less than four')

y = []
y.append(1)
y.append(5)
print(y)

for q in y:
    print(q)

#get input from standard input using the "input()" function

user_input = input('prompt: ')

print(user_input)

print('done')
