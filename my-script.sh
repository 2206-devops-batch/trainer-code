#!/usr/bin/bash

# ^ that's called the "shebang" - it defines what program
# should be used to interpret/execute this file's lines

# any other line that starts with a hash sign # is a comment

echo welcome to my script
touch new-file.txt
cd doesntexist
echo exiting...

# every program has some numerical exit code
# typically between -128 and 127

# 0 means success, no error
# anything else means an error

# we have ; && ||
# to control execution of multiple commands
# based on exit code

# a shell script like this one inherits the exit code
# of the last command to run inside it.
# it ignores the exit codes of any commands before that!

# we can do "if statements" in here
if echo hello
then
echo other commands
echo other commands
fi

# if the exit code of the command after "if" is 0, it will run
# what's between "then" and "fi", otherwise it will skip it.

# a lot of the time, the convenient command to use for this purpose
# is a special command called "test", or written "[" or "[["
# (those are all subtly different unfortunately)

abc=5
if [[ $abc == 5 ]]
then
echo five
fi

