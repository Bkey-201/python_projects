# num=2.0
# num2 = 2.2
# print(num.is_integer(), num2.is_integer())
# print(num2.is_integer())

# Напишите программу, которая предлагает пользователю ввести число,
# а затем выводит его округленным до двух цифр. Выполнение вашей программы должно выглядеть примерно так:
# user= input('Enter а number: ')
# userout= float(user)
# otvet = str(user) + ' rounded to 2  decimal places is ' + str(round(userout, 2))
# print(otvet)
# Напишите программу, которая предлагает пользователю ввести число,
# а затем выводит абсолютное значение этого числа. Выполнение вашей
# программы должно выглядеть примерно так:
# The absolute value of -10 is 10.0
# user1= input('Enter а number: ')
# userout1= float(user1)
# otvet1 = ' The absolute value of ' + str(user1) + ' is ' + str(abs(userout1))
# print(otvet1)
# Напишите программу, которая предлагает пользователю ввести два числа, используя input () дважды, а затем сообщает, является ли разность
# этих двух чисел целым числом. Выполнение вашей программы должно
# выглядеть примерно так:
# user2= input('Enter а number: 1.5')
# usr2= float(user2)
# user3=input('Enter another number: .5')
# usr3=float(user3)
# raznost=usr2-usr3
# trans= usr2.is_integer() + usr3.is_integer()
# trans1=raznost.is_integer()
# # otvet3 = 'The difference between' + usr2.is_iteger()+ ' and '+ usr3.is_integer() + 'is an integer? True!'
# otvet3 = 'The difference between' + str(usr2)+ ' and '+ str(usr3) + 'is an integer?' + str(trans1)
# print(otvet3)
user4= input('Enter а number: 1.5')
usr4= float(user4)
user5=input('Enter another number: .5')
usr5=float(user5)
raznost1=usr4-usr5
raznost1=usr4+usr5
trans2=raznost1.is_integer()
# otvet3 = 'The difference between' + usr2.is_iteger()+ ' and '+ usr3.is_integer() + 'is an integer? True!'
otvet3 = 'The difference between' + str(usr4)+ ' and '+ str(usr5) + 'is an integer?' + str(trans2)
print(otvet3)