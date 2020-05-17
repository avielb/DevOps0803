print(list(range(10)))

names = ["David", "Haim", "John", "Avner"]

for i in range(4):
    print(names[i])

for name in names:
    print("Hello: " + name)

for i in range(1, 101):
    if i%2 == 0:
        continue
    else:
        print(i)

for i in range(1, 101):
    print(i)
    if i == 78:
        break
else:
    print("everything finished successfully")

for i in range(1, 101):
    if i % 7 == 0:
        print("Boom")
        continue
    print(i)
