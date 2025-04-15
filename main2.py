# what are variables

# there are different types of variables
# strings are text
name = "John" #quotation marks
name2 = "Lucy"
# integers are whole numbers
num1 = "10" # no quotation marks
num2 = 20
print(int(num1) + num2) # when you have
# a plus sign between two variables its called
#concatentation
#type casting when you convert a 
# variable from one type to another
print(name + "and" + name2 + "have" + num1 + str(num2) + "apples")
#f strings allow us to insert variables into strings
# using f before the string
print(f"{name} and {name2} have {num1 + num2} apples")

# floats are decimal numbers
dollars = 10.99
# it can be positive or negative
print(f"{name} has {dollars} dollars")
# booleans are true or fale
is_student = True
# it can be true or false
print(f"{name} is a student: {is_student}")
# lists are collections of values 
# dictionaries are collections of key-value pairs
#problem set #1
# 1. create 4 differnet types of variables
# 2. print them out
# 3. use f strings to format the strings


# if conditionals
# if statements are used to check if a condition is ture or false
# if condition is true, do something
# if condition is false, do something else

# if conditional statements always start with if
# and depend on a boolean value (true or false)
# example
classStarted = True #boolean variable
if classStarted:
    print("class has started")
else:
    print("class has not started")

# logical abd comparison operators
# == equal to
# != not equal to
# > greater then
# < less than
# >= greater than or equal to
# <= less than or equal to
# and logical operators
# or logical operators
# not logical operators
# example
age = 18
if age >= 18:
    print("you are an adult")
elif age == 17:
    print("you are almost an adult")
else:
    print("you are a minor")

# problem set #2
# 1. create a program tgar checks if number
# is even or odd
# 2. ask user for a number
number = int(input("what is your number"))
# 3. check if number is even or odd
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")