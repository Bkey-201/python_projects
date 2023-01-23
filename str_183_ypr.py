import random
# Напишите функцию roll( ), которая использует randint() для моделрования броска симметричного кубика, возвращающего случайное целое
# число от 1 до 6.
# def roll(a, b):
#     if random.randint(a, b)==-1:
#         return random.randint(a, b)
#     # elif random.randint(1, 6)==2
# a=1
# b=6
# print(roll())
#     f = random.randint(1, 6)
#     # print(f)
# print(roll())
def roll():
    a=random.randint(1, 6)
    return a
print(roll())