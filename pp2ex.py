'''practicepython.org ex2
Ask the user for a number.
Depending on whether the number is
even or odd, print out an appropriate message to
the user. Hint: how does an even / odd number react
differently when divided by 2?
'''

number = int(input("Pick a number: "))
checker = int(input("Pick a secodn number!: "))
if number % 4 == 0 :
    print("Your number is divisible by 4!~")
elif number % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is odd :(")

if checker % number == 0:
    print("your second number is divisible by your first number!")
else:
    print("Your second number ain't divisible by the first.")
