
def summ_num(num):
    summ = 0
    while num > 0:
        digit = num % 10
        if digit !=0:
            summ = summ + digit
        num = num // 10
    return summ

def amount_num(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count


n = int(input('Введите число: '))

summ = summ_num(n)
amount = amount_num(n)

print(summ)
print(amount)
print(summ - amount)