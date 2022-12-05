list_one = []
list_two = []

for i in range(3):
        query = 'Введите ' + str(i + 1) + ' число для первого списка: '
        number = int(input(query))
        lst_one.append(number)

for i in range(7):
        query = 'Введите ' + str(i + 1) + ' число для второго списка: '
        number = int(input(query))
        lst_two.append(number)

print('Первый список:', list_one)
print('Второй список:', list_two)

list_one.extend(lst_two)
for _ in range(len(lst_one)):
        for i in lst_one:
                if lst_one.count(i) > 1:
                        lst_one.remove(i)
print('Новый первый список с уникальными элементами:', lst_one)
