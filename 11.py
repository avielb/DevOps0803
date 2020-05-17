myfile = open("read_my_contents.txt", "r")
all_lines = myfile.readlines()
for line in all_lines:
    print(line, end='')

myfile.close()

my_new_file = open("my_file.txt", "w")
my_new_file.write("Hello my file....")
my_new_file.close()

my_other_file = open("read_my_contents.txt", "a")
my_other_file.write("\nthis is the last line")
my_other_file.close()
