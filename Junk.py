import os


dir_name = 'python_basic'
main_script = open('scripts.txt', 'a')
sep_line = '*' * 40 + '\n'

for i_script in os.listdir(dir_name):
    open_file = open(os.path.join(dir_name, i_script), 'r')
    for i_string in open_file.read():
        main_script.write(i_string)
    open_file.close()
    main_script.write(sep_line)

main_script.close()

