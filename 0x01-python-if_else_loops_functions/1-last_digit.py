#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#get last digit of number
last_digit = abs(number) % 10

if last_digit > 5: 
    print(f"last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"last digit of {number} is {last_digit} and is zero")
elif (last_digit < 6) and (last_digit != 0):
    print(f"last digit of {number} is {last_digit} is less than 6 and not 0")
