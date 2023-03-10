capitals = {
"California": "Sacramento",
"New York" : "Albany",
"Texas": "Austin",}
print(capitals)

key_value_pairs = (
("California", "Sacramento"),
("New York", "Albany"),
("Texas", "Austin"),)
capitals1 = dict(key_value_pairs)
print(capitals1)

print(capitals["Texas"])

#Добавим столицу Колорадо в словарь capitals:
capitals['colardo'] = 'Denver'
print(capitals)
capitals['Texas'] = 'Houston'
print(capitals)

del capitals['Texas']
print(capitals)

# print(capitals['Arizona'])
if 'California' in capitals:
    print('Имеется в списке ')
else:
    print('No Имеется в списке')