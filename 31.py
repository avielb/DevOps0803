import pymysql

connection = pymysql.connect(host='database-1.c65uwrrkzb8g.us-east-1.rds.amazonaws.com', port=3306,
                             user='admin', passwd='Aa123123', db='aviel', autocommit=True)

# get new cursor
cursor1 = connection.cursor()

def new_animal(cursor_to_execute):
    name_of_animal = input("enter animal name: ")
    type_of_animal = input("enter animal type: ")
    age_of_animal = int(input("enter animal age: "))
    cursor_to_execute.execute(f"insert into animals values ('{name_of_animal}','{type_of_animal}',{age_of_animal})")

def delete_animal(cursor_to_execute, animal_name):
    cursor_to_execute.execute(f"delete from animals where name = '{animal_name}'")
#new_animal(cursor1)

def show_animals(cursor_to_execute):
    cursor_to_execute.execute("select * from animals")
    for row in cursor_to_execute:
        print(f"name is {row[0]}, age is: {row[2]}, from type: {row[1]}")

#delete_animal(cursor1, "rexi")
new_animal(cursor1)
new_animal(cursor1)
show_animals(cursor1)