#define operators
def addition:
    return integer1 + integer2
def subtraction:
    return integer1 - integer2
def multiplication:
    return integer1 * integer2
def division:
    return integer1 / integer2
#def simple calculator main function and print prompt
print ("This program is designed to function as a simple calculator. This program can perform Addition, Subtraction, Multiplication, and Division.")
#take input from user.
while true:
    operation = input("What do you want the program to solve? 1 - Addition. 2 - Subtraction. 3 - Multiplication. 4- Division. ")
    if operation in ('1', '2', '3', '4'):
        try:
            integer1 = int(input('Input the first integer: '))
            integer2 = int(input('Input the second integer: '))
        except ValueError:
            print ("There seems to be an error. Are you sure you entered an integer?")
            continue
        

#ask user if they want to try again