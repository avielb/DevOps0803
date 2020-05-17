from .age import get_age

try:
    get_age()
except ValueError as e:
    print("failed to get age because of: " + str(e.args))