from math import factorial as factorial_module


## v.1 - with local factorial function
# def factorial_local(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial_local(n - 1)
#
# def calculating_math_func_local(data):
#     return ((factorial_local(data)) / data ** 3) ** 10

## v.2 - with factorial from module 'math'
def calculating_math_func_module(data):
    return ((factorial_module(data)) / data ** 3) ** 10


number = int(input('Ввести число: '))
# print(calculating_math_func_local(number))
print(calculating_math_func_module(number))
