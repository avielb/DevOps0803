try:
    print(1/0)
except ValueError as e:
    print("bla")
except ZeroDivisionError as e:
    print("blu")
finally:
    print("this happened")