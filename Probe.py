original_dict = {
    ' ': 2,
    '-': 1,
    'З': 1,
    'а': 2,
    'д': 1,
    'е': 1,
    'и': 1,
    'н': 2,
    'о': 3,
    'п': 1,
    'с': 2,
    'т': 2,
    'ч': 1,
    'ь': 1
}

invert_dict = dict.fromkeys(original_dict.values())

for i_key in invert_dict:
    invert_dict[i_key] = []
    for i_sym in original_dict:
        if original_dict[i_sym] == i_key:
            invert_dict[i_key].append(i_sym)

print('Инвертированный словарь частот:')
for i_num in sorted(invert_dict.keys()):
    print(i_num, ':', invert_dict[i_num])
