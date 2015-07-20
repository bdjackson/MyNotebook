def compress_string(in_string):
    out_string = [in_string[0]]
    current_char = in_string[0]
    current_count = 1

    for ch in in_string[1:]:
        if ch == current_char:
            current_count += 1
        else:
            out_string.append(str(current_count))
            current_char = ch
            out_string.append(current_char)
            current_count = 1

    out_string.append(str(current_count))

    if len(out_string) > len(in_string):
        return in_string
    return ''.join(out_string)

print compress_string('aaabcccccaaa')
