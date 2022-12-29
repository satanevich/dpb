s = {}
while True:
    print('Введите номер действия:\n \
    1. Добавить контакт \n \
    2. Найти человека')
    d = input()
    if d == '1':
        name = input('Введите имя и фамилию нового контакта (через пробел): ').lower().split()
        if (name[0].capitalize(), name[1].capitalize()) in s:
            print('Такой человек уже есть в контактах.')
        else:
            s[(name[0].capitalize(), name[1].capitalize())] = \
            int(input('\nВведите номер телефона: '))
        print('Текущий словарь контактов: ', s)

    elif d == '2':
        for i, v in s.items():
            name2 = input('Введите фамилию для поиска: ').capitalize()
            if name2 == i[1][:len(name2)]:
                print(i[0].capitalize(), i[1].capitalize(), v)
