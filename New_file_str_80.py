name = "Zaphod"
heads = 2
arms = 3
kak = 2
# g=input('Введите 1 число:')
# g1=input('Введите 2 число')
# S=float(g)*float(g1)
# h=name + " has " + str(heads) + " heads and " + str(arms) + " arms" +str(S)
# print(h)
# 81 страница Упрощение команд вывыволда
L = name + " has " + str(heads) + " heads and " + str(arms) + " arms"
print(L)
m = f"{name} has {heads} heads and {arms} arms"
print(m)
n = 3
k = 4
let =f"{n} times {k} is {n*k}"
print(let)

ket= "{} has {} heads and {} arms".format(name, heads, arms,)
print(ket)
# Создайте переменную с плавающей точкой weight, содержащую значение
# 0. 2, и строковый объект animal со значением "newt". Выведите следующую
# строку с этими переменными, используя только конкатенацию строк:

# # perem = 0.2
# perem1= 'weight'
# perem2 = 'newt'
# print(str(perem) + ' kg is the ' + perem1 + ' of the ' + perem2)

weight = 0.2
animal= 'newt'
print(str(weight) + ' kg is the ' + 'weight' + ' of the ' + animal)
# выведите ту же строку с использованием метода . format () и пустых
# заполнителей {}.
print('{} kg is the {} of the {}'.format(str(weight), weight, animal))
print(f"{weight} kg is the {weight} of the {animal} ")
# 0.2 kg is the weight of the newt.