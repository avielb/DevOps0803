# define a function that it's input is 2 variables
# the function will return the sum of two numbers
def add_numbers(first_number, second_number):
    return first_number + second_number


# input for two numbers, we will ask for input and cast the numbers
x = int(input("enter first number: "))
y = int(input("enter second number: "))

# get result of adding the two numbers
result = add_numbers(x, y)

# print the result
print("addition result is: " + str(result))
