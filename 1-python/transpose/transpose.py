def transpose_(lines):
    input_list = lines.split('\n')  # or splitlines
    input_height = len(input_list)
    input_width = get_input_width(input_list)

    output_list = []

    for colnum in range(input_width):
        output = ''
        for rownum in range(input_height):
            output += get_char(input_list, rownum, colnum)
        # output = output.rstrip('*').replace('*', ' ')
        output_list.append(output)

    return '\n'.join(output_list)

def get_input_width(input_list):
    return 0

def get_char(input_list, rownum, colnum):
    return ' '

# print(transpose('ABC\nDEF'))
# print(transpose('ABC\nDE'))
# print(transpose('AB\nDE'))

# turn "ABC\nDEF"
# into: "AD\nBE\nCF"
