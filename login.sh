#!/usr/bin/env bash

correct_username=nick
correct_password=password123

echo Enter username:

read username_input

echo Enter password:

read password_input

if [[ $username_input == $correct_username ]]; then
	if [[ $password_input == $correct_password ]]; then
		echo Success, you are logged in
		exit 0
	fi
fi

echo Username or password incorrect
exit 1
