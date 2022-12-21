text = input('Введите строку: ').split()

max_len = [len(i) for i in text]
max_word = text[max_len.index(max(max_len))]

print('Самое длинное слово: {}\nДлина этого слова: {}'.format(max_word, len(max_word)))

