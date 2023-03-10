colors = ["red", "yellow", "green", "Ыuе"]
# Вставляет "orange" во вторую позицию
colors.insert(1, "orange")
print(colors)
print('.pop получает один параметр - индекс i - и удаляет из списка значение в позиции с заданным индексом')
color = colors.pop(3)
print(color)# удаляет green
print(colors) #удаляет blue
# colors.pop(-1) #удаляет конечный объект списка
# print(colors)
colors.pop()#без условия удаеляет последний объект
print(colors)
colors.append("indigo") #Mетод list. append () используется для добавления нового элемента в конец списка:
print(colors)
colors.extend(["violet", "ultraviolet"]) #Метод list. extend () используется для добавления нескольких новых элеменtов в конец списка:
print(colors)