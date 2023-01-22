sum_of_evens = 0 #присваетваться к переменная значения 0
#пока n-ое значение в диапозоне чисел от 0 до 101(не вкл 101)
for n in range(101):
    if n % 2 == 0:
        sum_of_evens = sum_of_evens + n
print(sum_of_evens)


# a=10
# for k in range(5):
#     b=a+1
# print(b)
#
# for i in range(1, 6, 2):
#     print(i)

# word = "hello world"
# for i in word:
#     print(i*3)
# count = 0
# word = "hello world"
# for i in word:
#     if i == 'l':
#         count += 1
#         print('Yes')
# print('Count:', count)