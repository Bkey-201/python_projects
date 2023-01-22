# try:
#     number = int(input("Enter ап integer: "))
# except ValueError:
#     print("That was not ап integer")
#
# number = int(input("Enter ап integer: "))
# print("уууу")


def divide(num1, num2):
    try:
        print(num1 / num2)
    except (TypeError, ZeroDivisionError):
        print("encountered а proЫem")

num1=int(input('Введите число 1: '))
num2=int(input('Введите число 2: '))

f=divide(num1, num2)
print(f)

