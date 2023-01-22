# Упражнения
# 1. Используя команду break, напишите программу, которая многократно
# запрашивает у пользователя данные и завершается только тогда, когда
# пользователь введет "q" или "Q".
#
# for n in range(3):
#     password = input("Введите Password: ")
#     if password == "q" or password == "Q":
#         break
#     print("Password is incorrect.")
# else:
#     print("Suspicious activity. The authorities have Ьееп alerted.")

#  Используя команду continue, напишите программу, которая перебирает
# числа от 1 до 50 и выводит все числа, не кратные 3.
for s in range(1,50):
    if s % 3 != 0:
        print(s)

for s1 in range(1,50):
    if s1 % 3 == 0:
        continue
    print(s1, end =' ')#выводит в строчку результат ,а не в столбец на экран
print('www')
