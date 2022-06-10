# first argument: path
# second argument: "mode" - ("r" for read-only, "w" for write, "a" for append)
# returns: "file object"
# datafile = open('data.txt', 'w')
# most commonly used stuff on files:
# for line in file:
#     pass # iterating file gives each line in the file.
# datafile.read(): read the whole contents of the file in one string.
# datafile.readlines(): read all lines into a list in one step
# for writing....
# datafile.write(str): write a string to the file
# print(thing, file=datafile): write something converted to a string to the file
# datafile.close(): close the file when done.

# try:
#     potentially_failing_code()
#     code() # if and only if the code throws no errors
# except IOError:
#     code()  # if and only if the code throws an IOError specifically
# finally:
#     code()  # runs literally always (handled error, unhandled error, no error)

# code()  # if and only if the code does not throw some OTHER error besides IOError

with open('data.txt', 'w') as file:
    file.write('hello')

with open('data.txt') as file:
    for line in file:
        print(line)

# the file has definitely been closed even if an error was thrown

# namespaces in python

# a namespace is a context where variables live
# the way that python interprets any name of a variable/etc
#  like fred, Person, print, str, etc
# LEGB namespaces
# first, it checks the local namespace
# then, any enclosing namespaces,
# then, the global namespace,
# then, the built-in namespace (print, str)

var = 5  # global
if True:
    var2 = 5  # global

# functions, including nested functions, have their own namespaces


def func():
    var = 6  # enclosing (relative to func2)
    func2()

    # def print():
    #     pass

    def func2():
        var = 7  # local
        # print = 5
        print(var)
        # id = 5
        # map
        # filter

func()
