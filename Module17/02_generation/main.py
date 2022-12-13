length_list = int(input('Введите длину списка: '))
result = [x % 5 if x % 2 else 1 for x in range(length_list)]
print(result)
