def get_gcd(a):
    gcd = 1
    for i in range(1, a + 1):
        if a % i == 0:
            gcd = i
        if gcd > 1:
            break
    return gcd


number = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', get_gcd(number))

