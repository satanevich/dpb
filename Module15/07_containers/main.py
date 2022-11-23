i = 0
l = []
number = int(input('Количество контейнеров: '))
for _ in range(number):
    l.append(int(input('Введите вес контейнера: ')))
k = int(input('\nВведите вес нового контейнера: '))
while i < len(l) and l[i] >= k:
    i += 1
print('\nНомер, куда встанет контейнер:', i + 1)
