nums = [1, 2, 3, 4, 5]
total = 0
for number in nums:
    total = total + number
    print(total)
print(total)
print(sum([1, 2, 3, 4, 5]))

print(min([1, 2, 3, 4, 5]))

print(max([1, 2, 3, 4, 5]))

print(sum((1,2,3,4,5)))
print(min((1,2,3,4,5)))
print(max((1,2,3,4,5)))

numbers = (1,2,3,4,5)
squares =[num**2 for num in numbers]
print(squares)

squares = []
for num in numbers:
    squares.append(num**2)
    print(num)
    print(squares)
print(squares)

str_numbers = ["1.5", "2.3", "5.25"]
print(type(str_numbers))
float_numbers = [float(value) for value in str_numbers]
print(type(float_numbers))
print(float_numbers)