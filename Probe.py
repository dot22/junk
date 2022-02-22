def user_script(string):
    user_list = [i_sym for i_num, i_sym in enumerate(string) if i_num % 2 == 0]
    return user_list

string1 = 'О Дивный Новый мир!'
string2 = [100, 200, 300, 'буква', 0, 2, 'a']
print(user_script(string1))
print(user_script(string2))
