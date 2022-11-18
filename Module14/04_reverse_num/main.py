def separation_whole(number):
    flag = True
    whole = ""
    fraction = ""
    for symbol in number:
        if symbol == '.':
            flag = False
        elif flag:
            whole = whole + symbol
        else:
            fraction = fraction + symbol
    return int(whole)

def separation_fraction(number):
    flag = True
    whole = ""
    fraction = ""
    for symbol in number:
        if symbol == '.':
            flag = False
        elif flag:
            whole = whole + symbol
        else:
            fraction = fraction + symbol
    return int(fraction)

def revers(n):
    count = 0
    while n > 0:
        count = count * 10 + n % 10
        n //= 10
    return str(count)

def bonding(revers_whole, revers_fraction):
    revers_num = revers_whole + "." + revers_fraction
    return str(revers_num)

def summ_mun(first_num, second_num):
    summ = float(first_num) + float(second_num)
    return summ

first_number = (input("Введите первое число: "))
second_number = (input("Введите второе число: "))

print(f"\nПервое число наоборот: {bonding(revers(separation_whole(first_number)), revers(separation_fraction(first_number)))}"
f"\nВторое число наоборот: {bonding(revers(separation_whole(second_number)), revers(separation_fraction(second_number)))}")

print(f"\nСумма: {summ_mun(bonding(revers(separation_whole(first_number)), revers(separation_fraction(first_number))), bonding(revers(separation_whole(second_number)), revers(separation_fraction(second_number))))}")


