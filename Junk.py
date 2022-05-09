speakers_file = open('speakers.txt', 'r', encoding='utf')
# data = speakers_file.read()
# print(data)
for i_line in speakers_file:
    print(i_line, end='')
speakers_file.close()
