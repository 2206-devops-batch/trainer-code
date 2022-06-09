#!/usr/bin/env bash

echo $0
echo $1
echo $2
echo $@

# in bash, almost everything is just text

x=5
y="5"


# we do have arrays with ( )
# we also have "associative arrays" that we can declare
#   that operate on key-value pairs

reusable_function () {
    echo asdf
    echo $1
}

reusable_function whatever

for z in 1 2 3 4 ; do
	reusable_function $z
done

# for (())

# substitute the result of a command into the text of another command
# typically with $()
current_date=$(date)
echo $current_date
