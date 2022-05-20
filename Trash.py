def collect_stats(file_name):
    result = {}
    text_file = open(file_name, 'r', encoding='utf-8')
    for i_line in text_file:
        for j_char in i_line:
            if j_char.isalpha():
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] += 1
    text_file.close()
    return result


def print_stats(stats):
    print("+{:-^19}+".format('+'))
    print("|{: ^9}|{: ^9}|".format('буква', 'частота'))
    print("+{:-^19}+".format('+'))
    for char, count in stats.items():
        print("|{: ^9}|{: ^9}|".format(char, count))
    print("+{:-^19}+".format('+'))


def sort_by_freq(stats_dict):
    sorted_values = sorted(stats_dict.values())
    sorted_dict = {}
    for i_values in sorted_values:
        for j_key in sorted_dict.keys():
            if stats_dict[j_key] == i_values:
                sorted_dict[j_key] = stats_dict[j_key]
    return sorted_dict


file_name = 'voyna-i-mir.txt'
stats = collect_stats(file_name)
stats = sort_by_freq(stats)
print_stats(stats)
