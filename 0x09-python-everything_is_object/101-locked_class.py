#!/usr/bin/python3
locked_class = LockedClass()

locked_class.frist_name = "Bob"
try:
    locked_class.last_name = "Doe"
except AttributeError as e:
    print(e)

try:
    locked_class.age = 30
except AttributeError as e:
    print(e)

try:
    locked_class.first_name = "Jane"
except AttributeError as e:
    print(e)
