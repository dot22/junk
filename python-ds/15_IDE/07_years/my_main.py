def year(date1, date2):
    for i in range(date1, date2 + 1):
        compare(i)
    return


def compare(number):
    n1 = number % 10
    n2 = number // 10 % 10
    n3 = number // 100 % 10
    n4 = number // 1000
    if n1 == n2 and n1 == n3 or n1 == n2 and n1 == n4 or n2 == n3 and n2 == n4:
        print(number)
    return


year1 = 1900
year2 = 2100
year(year1, year2)
