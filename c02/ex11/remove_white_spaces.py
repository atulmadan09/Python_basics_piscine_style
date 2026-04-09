def ft_strlen(string):
    length = 0
    for i in string:
        length = length + 1
    return length

def remove_white_spaces(string):
    answer= ft_strlen(string)
    dest = ""
    for i in range(0, answer):
        if (string [i] != ' '):
            dest = dest + string[i]
    return dest

N = input("Please input the string: ")

answer1 = remove_white_spaces(N)
print(f"The new string without any space is '{answer1}'")
