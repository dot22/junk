def isprime(amount):
    summ = 0
    for order in range(amount):
        a = int(input("Введите число: "))
        flag = 0
        for i in range(2, a // 2 + 1):
            if a % i == 0:
                flag = 1
                break
        if flag == 0:
            summ += 1
    print('Summ =', summ)


numbers = int(input('Введите количество чисел: '))
isprime(numbers)
