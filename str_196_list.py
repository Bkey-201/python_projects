print(list((1,2,3)))
print(list("Pyton"))
groceries = "eggs, milk, cheese"
grocery_list = groceries.split(";")
print(grocery_list)
s ="a;b;c".split(";")
print(s)
numbers= [1,2,3,4]
print(numbers[1])
print(numbers[1:3])
print("Воb" in numbers)
for number in numbers:
    if number %2 ==0:
        print(number)

colors = ["red", "yellow", "green", "Bluе"]
colors[0] = "burguпdy"
print(colors)

colors[1:3] = ["orange", "magenta"]
print(colors)


colors = ["red", "yellow", "green", "Bluе"]
colors[1:3] = ["orange", "magenta", "aqua"]
print(colors)

colors[1:4] = ["yellow", "green"]
print(colors)

colors = ["red", "yellow", "green", "Ыuе"]
# Вставляет "orange" во вторую позицию
colors.insert(1, "orange")
print(colors)

colors.insert(10, "violet")
print(colors)

colors.insert(-1, "indigo")
print(colors)

colors1 = colors.insert(-1, "indigo")
print(colors)

color6 = colors.pop(3)
print(color6)
print(colors)