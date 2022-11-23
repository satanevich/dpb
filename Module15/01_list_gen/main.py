number_list = []
number = int(input('Введите число: '))

for i in range(1, number+1, 2):
    if i % 2 != 0:
        number_list.append(i)

print('Список из нечётных чисел от одного до N:',number_list)
