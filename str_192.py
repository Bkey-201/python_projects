vowels =("а", "е", "i", "о", "u")
for vowel in vowels:
    print(vowel.upper())

# for <переменная> in <последовательность>:
#     <действие>
# else:
#     <действие>

languages = ("C", "C++", "Perl", "Python")
for x in languages:
    print(x)

languages = ("Привет Всем")
for x in languages:
    print(x*10)

#вывести строку 10 раз
languages = ("Привет Всем")
for x in range(1,11):
    print(languages)

#цикл while
# i = 2
# while i <= 10:
#     print(i)
#     # i+=1
#     i = 1 + i
# print(i)
#
# i = 1
# while i <= 10:
#     i += 1
#     print(i)
# print(i)


# i = 0
# while i <= 10:
#     i=1+i
#     print(i)