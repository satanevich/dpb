def main():
    names_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
    first = []
    for i in range(1, len(names_list), 2):
        first.append(names_list[i])
    print('Первый день:', first)

main()