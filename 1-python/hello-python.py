# with python you execute "statements".
# "simple statements" are the ones that fit in one line.
# for example: assigning a variable
x = 6
# within a statement there can be "expressions"
# an expression is a piece of python syntax that "evaluates" to some value.
# python applies things like operators and functions to evaluate expressions
# as part of executing the statement they're contained in.
x = (1 + 2 + 3)
x += 1 # increment x by 1

# "compound statements" are the statements that involve a "block" of indented lines
# introduced by a colon character (:)
# if statement
# while statement
# for statement
# try statement
# function definitions
# class definitions


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
elif 3 > 4:
    print('three greater than four')
else:
    print('three equal to four')


y = []
y.append(1)
y.append(5)
print(y)

for q in y:
    print(q)

#get input from standard input using the "input()" function

user_input = 0
while user_input <= 99:
    try:
        user_input = int(input('enter a number greater than 99: '))
    except ValueError:
        pass

# "handling errors in python":
# 1. find a way to check if there will be an error before you act
#      (if statement)
# 2. just try doing the thing, and handle an error if it happens
#      (try statement)

print(user_input)

print('done')

def reverse_string(s):
    x = list(s)
    x.reverse()
    return ''.join(x)

def reverse_string_2(s):
    # return ''.join(reversed(s))
    return s[::-1]

print(reverse_string_2('asdf'))
