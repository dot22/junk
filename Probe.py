test = input('Введите данные: ')

if isinstance(test, str):
    print('Тип данных: str (строка)')
    print('Неизменяемый (immutable)')
elif isinstance(test, list):
    print('Тип данных: list (список)')
    print('Изменяемый (mutable)')
elif isinstance(test, dict):
    print('Тип данных: dict (словарь)')
    print('Изменяемый (mutable)')
elif isinstance(test, set):
    print('Тип данных: set (множество)')
    print('Изменяемый (mutable)')
elif isinstance(test, bool):
    print('Тип данных: Bool (логический)')
    print('Неизменяемый (immutable)')
else: # isinstance(test, tuple):
    print('Тип данных: tuple (кортеж)')
    print('Неизменяемый (immutable)')
print('ID объекта:', id(test))