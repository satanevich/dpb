cell_list = [3, 0, 6, 2, 10]
cell_range =[]
print('Количество клеток: ', len(cell_list))

for i in range (len(cell_list)):
    print('Эффективность', i + 1, 'клетки', cell_list[i])
    if i > cell_list[i]:
        cell_range.append(cell_list[i])

print('\nНеподходящие значения:', cell_range)

