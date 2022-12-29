zen_file = open('zen.txt', 'r')

zen_read = zen_file.read()
zen_read_list = zen_read.split('\n')

for i_string in zen_read_list[::-1]:
    print(i_string)

zen_file.close()
