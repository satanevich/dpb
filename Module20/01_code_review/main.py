def foo(d: dict) -> tuple:
    return set(sum([d[i]['interests'] for i in d], [])), sum(map(len, [d[i]['surname'] for i in d]))

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}
pairs = []
for i in students:
    pairs += (i, (students[i]['age']))

print('Список пар "ID студента — возраст":', pairs)
interests, total_len = foo(students)
print('Полный список интересов всех студентов:', ', '.join(interests))
print('Общая длина всех фамилий студентов:', total_len)

# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)