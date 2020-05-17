isTrue = False
a = 5
b = 2.5
strOne = "One"
strThree = "Three"
my_name = "Aviel"
names = ["David", "Haim", "John", "Avner"]

if a <= b or strOne == "One":
    print(a <= b)
    print(strOne == "One")
    print("a is smaller equal than b")
    print("a is definitely smaller equal than b")

if "Haim" in ["David", "Haim", "John", "Avner"]:
    print("we found it")
else:
    print("we didn't find it")


if len(names) < 3:
    print("we don't have enough names")
elif len(names) >= 3:
    print("we have enough names in the list")

x = 5
y = 5
if type(x) is :
    print(type(x))

x = [1, 2, 3]
y = x
print(x == y) # Prints out True
print(x is y) # Prints out False

# if keys