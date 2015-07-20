def string_replace(in_string, trun_len):
    char_list = [ch for ch in in_string]
    if len(char_list) > trun_len:
        char_list = char_list[:trun_len]
    for i, ch in enumerate(char_list):
        if ch == ' ':
            char_list[i] = '%20'
    return ''.join(char_list)

def string_replace_v2(in_string, true_len):
    return ''.join([ch if ch != ' ' else '%20' for ch in in_string[:true_len]])

print string_replace('Mr John Smith', 13)
print string_replace('Mr John Smith         ', 13)
print string_replace('Mr John Smith         ', 15)

print

print string_replace_v2('Mr John Smith', 13)
print string_replace_v2('Mr John Smith         ', 13)
print string_replace_v2('Mr John Smith         ', 15)
