def count_number(checked_year):
    digit_1 = checked_year // 1000
    digit_2 = checked_year // 100 % 10
    digit_3 = checked_year % 100 // 10
    digit_4 = checked_year % 10
    # возможно, для улучшения читаемости кода, не стоит делать такие большие условия в одном блоке, но создать несколько блоков elif.
    if (digit_1 == digit_2 and (digit_1 == digit_3 or digit_1 == digit_4) and digit_3 != digit_4) \
            or (digit_1 != digit_2 and digit_1 == digit_3 and digit_1 == digit_4) \
            or (digit_2 != digit_1 and digit_2 == digit_3 and digit_2 == digit_4):
        print(checked_year)


start_year = int(input('Введите первый год: '))
end_year = int(input('Введите второй год: '))

print('\nГоды от', start_year, 'до', end_year, 'с тремя одинаковыми цифрами')
for year in range(start_year, end_year + 1):
    count_number(year)

# зачёт!
