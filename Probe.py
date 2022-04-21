def find_file(cur_path, file_name):
    if key in struct:
        return struct[key]

    for sub_struct in struct(values):
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key)
            if result:
                break
    else:
        result = None

    return result
            l