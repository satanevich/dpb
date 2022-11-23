word = input('Введите слово: ')
letters = list(word)
unique_letters = 0
for i in letters:
    same_letters = 0
for j in letters:
    if j == i:
        same_letters += 1
    if same_letters == 1:
        unique_letters +=1

print('Количество уникальных букв:', unique_letters)