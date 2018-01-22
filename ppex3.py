'''practicepython.org ex3
Create a program that asks the user for a number and then
prints out a list of all the divisors of that number. (If you don’t
know what a divisor is, it is a number that divides evenly into another
number. For example,
13 is a divisor of 26 because 26 / 13 has no remainder.)

my_range = range(0,912341451)
my_divisor = int(input("What is your divisor?: "))
new_list = []

for i in my_range:
    if my_divisor % i == 0:
        new_list.append(i)

print(new_list)
'''


num = int(input("Please choose a number to divide: "))

listRange = list(range(1,98987987))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)
