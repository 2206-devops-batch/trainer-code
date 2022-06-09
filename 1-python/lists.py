# pythonic
def filter_all_gt_20(l):
    # list comprehension syntax
    return [n for n in l if n <= 20]

# unpythonic
def filter_all_gt_20_with_loops(l):
    result = []
    for n in l:
        if n <= 20:
            result.append(n)
    return result


data = [4,5,6,3,6,78,32,78,0,4,22]
data = filter_all_gt_20(data)

# print the first number greater than 20

# pretty unpythonic
i = 0
while i < len(data):
    if data[i] > 20:
        print(data[i])
        break
    i += 1

# python has a builtin function called "range"
# which returns a special data type called a range.
# a range represents a sequence of numbers with a start, an stop, and a step

# range(0, len(data)) is a range starting at 0 and ending at len(data) - 1
#   (inclusive of the start, exclusive of the end)
# also, if you pass just one argument, it is assumed to be the stop, with a start of 0

# slightly more pythonic
for i in range(len(data)):
    if data[i] > 20:
        print(data[i])
        break

# much more pythonic
for n in data:
    if n > 20:
        print(n)
        break

# another way, even more pythonic
# (using a generator expression)
try:
    print(next(n for n in data if n > 20))
except StopIteration:
    print('no item greater than 20')

print('this will run whether theres an error or not')
