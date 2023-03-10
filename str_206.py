
two_bу_two = [[1, 2], [ 3, 4]]
# two_by_two имеет длину 2
print(len(two_bу_two))
print(two_bу_two[0])
print(two_bу_two[1])
print(two_bу_two[1][0])

# animals = ["lion", "tiger", "frumious Bandersnatch"]
# large_cats = animals
# large_cats.append("Tigger")
# print(animals)

animals1 = ["lion", "tiger", "frumious Bandersnatch"]
large_cats1 = animals1[:]
print(large_cats1)
large_cats1.append("leopard") #Добовляем в конец списка, с помощью метода append
print(large_cats1)
print(animals1)
#
# a=100
# b=a
matrix1 = [[1, 2], [3, 4]]
matrix2 = matrix1[:]
matrix2[0] = [5, 6]
print(matrix2)
print(matrix1)