#Строковые методы и неизменяемость
name = "Picard"
#ВЕРХНИЙ РЕГИСТР
k=name.upper()
print(k)
print(name)
#print(k)
#НИЖНИЙ РЕГИСТР
starship = "AniMNals"
N= starship.lower()
print(N)
#Удаление пропусков из строки

tringl = "    Filet     Mignon"
# a=tringl.lstrip()
# print(a)

a=tringl.strip()
print(a)

tringl= "Becomes"
#Объединение строк
name = "Zaphod"
heads = 2
arms = 3
d=name + " has " + str(heads) + " heads and " + str(arms) + " arms"
kq=f"{name} has {heads} heads and {arms} arms"
print(d)
print(kq)

n = 3
m = 4
kk = f"{n} times {m} is {n*m}"
print(kk)

weight=0.2
animal = "newt"
vivod=f"{weight} kg is the weight of the {animal}."
print(vivod)

#Поиск подстроки в строке, вывод индекса первого вхождения; индексация начинается с 0,1,2 и т.д
phrase = "the  surprise is in here somewhere"
vivodpoisk=phrase.find("surprise")
print(vivodpoisk)

phrase = "the surprise is in here somewhere"
viv=phrase.find("surprise1")
print(viv)

my_story = "I'm telling you the truth; nothing but the truth!"
repl=my_story.replace("the truth", "lies11111")
print(repl)

next = "some of the stuff"
new_text = next.replace("some of", "all")
new_text = new_text.replace("stuff", "things")
print(new_text)

text1="Somebody said something to Samantha."
zamena = text1.replace("s", "x")
#zamena = text1.replace("S", "x")
print(zamena)

#Числа с плавающей точкой
print(type(True) )
k=1e6
print(k)
#Осататок от деления %
a=20 % 7
print(a)

#Вычисление с вводом пользовательским
# vvod1=float(input('Enter а base:'))
# vvod2=float(input('Enter an exponent: '))
# vivodinputivse=f'{vvod1} to the power of {vvod2} = {vvod1*vvod2}'
# print(vvod1,vvod2)
# # print(vvod1)
# # print(vvod2)
# print(vivodinputivse)
#page_99
k = 0.1 + 0.2
print(k)

num_letters = len("12345")
print(num_letters)



eturn_value = print("What do I return?")
#print(num_letters)

Schet_dlina_stroki=len("Здесь 14 d")
print(Schet_dlina_stroki)