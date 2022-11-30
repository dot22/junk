for i in range(10, 100):
    n10 = i // 10
    n1 = i % 10
    s = 3 * (n1 * n10)
    if i == s:
        print(i)