N = int(input('Сколько элементов в списке: '))
List = []
for i in range(N):
    el = int(input('Введите значение элемента: '))
    List.append(el)
K = int(input('Сдвиг: '))
print(List)

for x in range(K):
    index = 0
    save = List[index - 1]
for i in range(len(List) - 1):
    List[index - 1] = List[index - 2]
    index -= 1

List[0] = save

print(List)

