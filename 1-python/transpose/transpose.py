from this import d


def transpose(string_input = 'ABC\nDdEF'):
    str_list = string_input.split('\n')

    new_list = []

    # find longest line length?
    longest_str = max(str_list, key=len)

    for i in range(len(longest_str)):
        output_line = ''
        for text in str_list:
            try:
                output_line += text[i]
            except IndexError:
                output_line += '*'
        output_line = output_line.rstrip('*').replace('*', ' ')
        new_list.append(output_line)


    return '\n'.join(new_list)



print(transpose())
