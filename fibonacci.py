# print the first N fibonacci numbers
n = int(input('choose n: '))
a, b = 0, 1
exec('print(a);a, b = b, a + b;' * n)

# interpreted vs compiled

# interpreter

# compiler

# at the end of the day, the purpose of all programming
# languages is to tell the CPU what to do

# one way to set that up is:
# - two-step process. the code that the human writes
#    is translated into a lower-level form as a one-time
#    preparation step called "build" or "compile".
#    the result of that is what we distribute to users
#    and what we re-run every time we use the program.
#   we have "compile-time" and "run-time" environments

# - one-step process. the code the human writes
#    is provided to some "interpreter" program
#    basically line-by-line every time you want to
#    run it, and all translation to lower-level instructions
#    for the current system happens at that time.
#   there is no "compile-time". only "run-time"
