guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

command = ''
while True:
    print(f'Сейчас на вечеринке {len(guests)} человек:', guests)
    command = input('Гость пришел или ушел? ')
    if command == 'пора спать':
        break
    guest_name = input('Имя гостя: ')
    if command == 'пришел':
        if len(guests) >= 6:
            print(f'Прости, {guest_name}, но мест нет.')
        else:
            guests.append(guest_name)
            print(f'Привет, {guest_name}!')
    elif command == 'ушел':
        guests.remove(guest_name)
        print(f'Пока, {guest_name}!')
    print()

print('\nВечеринка закончилась, все легли спать.')
