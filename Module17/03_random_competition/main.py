import random

first_team = list(round(random.uniform(5, 10), 2) for i in range(20))
second_team = list(round(random.uniform(5, 10), 2) for i in range(20))
winners_team = list()
for i in range(len(first_team)):
    if first_team[i] > second_team[i]:
        winners_team.append(first_team[i])
    else:
        winners_team.append(second_team[i])

print('Первая команда: ', first_team)
print('Вторая команда: ', second_team)
print('Победители: ', winners_team)