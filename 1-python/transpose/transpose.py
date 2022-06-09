from this import d


def transpose(string_input):
    a = string_input[0]
    b = string_input[1]
    print(a)
    print(b)
    new_list = []

    # a is bigger or same size as b
    if len(a) >= len(b):
        for i in range(len(a)):
            new_list.append(a[i]+b[i])
        return new_list
    
    # b is bigger than a
    else:
        for i in range(len(b)):
            new_list.append(a[i]+b[i])
        return new_list





    # for i in range(len(string_input)):
    #     a = string_input[i]
    #     b = string_input


print(transpose(['ABC', 'DEF']))
