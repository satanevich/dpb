letters = 'аоиеёэыуюя'

text = input('Введите текст: ')
l = [c for c in text if c in letters]
print('Список гласных букв: ', l)
print('Длина списка: ', len(l))
