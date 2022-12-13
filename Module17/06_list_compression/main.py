import random

duration = int(input('Количество чисел в списке: '))

before = [random.randint(0, 2) for _ in range(duration)]
print('Список до сжатия:', before)

compress = [x for x in before if x > 0]
count = len(before) - len(compress)
after = compress[:] + [0 for _ in range(count)]

print('Список после сжатия:', compress)
