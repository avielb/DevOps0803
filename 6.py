my_global_var = 5
def my_own_printer(to_print):
    print(my_global_var)
    print("-------------------")
    print(to_print)
    print("-------------------")
    if 5 == 5:
        print("")

def my_other_function():
    print(my_global_var)

input_from_user = input("enter your name: ")

    my_own_printer("your name is: " + input_from_user)
