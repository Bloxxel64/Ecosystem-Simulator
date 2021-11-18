import sys
import os
import time
import math

print("Welcome to Ecosystem Simulator")
print("")
print("Which Ecosystem should be loaded?.")
print("")
print("1. African Savanna")
print("")
ecosystem = input(">: ")

if ecosystem == "1":
  os.system('python africansavanna.py')