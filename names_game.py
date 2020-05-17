def save_names():
    name_to_save = input("Enter name: ")
    names_txt = open("names.txt", "a")
    names_txt.write(name_to_save + "\n")
    names_txt.close()


def print_names():
    names_txt = open("names.txt", "r")
    for name in names_txt.readlines():
        print("hello mr. " + name, end='')
    names_txt.close()


for i in range(10):
    save_names()

print_names()

if 4 < 5 and 6 < 7:
    print("")