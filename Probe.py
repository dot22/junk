def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

num_fact = factorial(5)
print(num_fact)