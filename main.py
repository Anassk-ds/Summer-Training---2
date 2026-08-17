'''
Create a one package called as utlities
    calculator.py
    greetings.py

main.py 
import from utilities and use them


'''
from Utilities.calculator import add , sub
from Utilities.greetings import hello

print(hello("Anas"))

print("Addition:", add(10, 20))
print("Subtaction:", sub(30,12))


import math
print(math.__name__)
print(math.__doc__)

import math

import sys
print(sys.path)

print(dir(math))

#pip ---Python package manager

#1-sys
#Multiple_canteen --- numpy ---1.0
#College_library --- numpy --- 2.0
#College_bus --- numpy --- 1.5 version

#python Virtual Environment
 
 #python -m venv env
 
 #env\Scripts\Activate.ps1
 
 #set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

