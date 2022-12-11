list_one = []
list_two = []

for i in range(3):
        query = 'Введите ' + str(i + 1) + ' число для первого списка: '
        number = int(input(query))
        list_one.append(number)

for i in range(7):
        query = 'Введите ' + str(i + 1) + ' число для второго списка: '
        number = int(input(query))
        list_two.append(number)

print('Первый список:', list_one)
print('Второй список:', list_two)

list_one.extend(list_two)
for _ in range(len(list_one)):
        for i in list_one:
                if list_one.count(i) > 1:
                        list_one.remove(i)
print('Новый первый список с уникальными элементами:', list_one)
