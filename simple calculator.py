#define operators
def addition(integer1, integer2):
    return integer1 + integer2
def subtraction(integer1, integer2):
    return integer1 - integer2
def multiplication(integer1, integer2):
    return integer1 * integer2
def division(integer1, integer2):
    return integer1 / integer2
#def simple calculator main function and print prompt
print ("This program is designed to function as a simple calculator. This program can perform Addition, Subtraction, Multiplication, and Division.")
#take input from user.
while True:
    operation = input("What do you want the program to solve? 1 - Addition. 2 - Subtraction. 3 - Multiplication. 4- Division. ")
    if operation in ('1', '2', '3', '4'):
        try:
            integer1 = int(input('Input the first integer: '))
            integer2 = int(input('Input the second integer: '))
        except ValueError:
            print ("There seems to be an error. Are you sure you entered an integer?")
            continue

        if operation == '1':
            print("The sum of " , integer1, "and ", integer2, "is ", addition(integer1, integer2))

        elif operation == '2':
            print("The difference of " , integer1, "and ", integer2, "is ", subtraction(integer1, integer2))

        elif operation == '3':
            print("The product of " , integer1, "and ", integer2, "is ", multiplication(integer1, integer2))

        elif operation == '4':
            print("The quotient of " , integer1, "and ", integer2, "is ", division(integer1, integer2))


#ask user if they want to try again