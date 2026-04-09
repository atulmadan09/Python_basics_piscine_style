def ft_strlen(string):
    length = 0
    for i in string:
        length = length + 1
    return length

def ft_str_count_char(string, target):
    answer= ft_strlen(string)
    count = 0
    for i in range(0, answer):
        if (string [i] == target):
            count = count + 1
    return count

N = input("Please input the string: ")
ch = input("Please input the character to check: ")

answer1 = ft_str_count_char(N, ch)
if answer1 == 0:
    print(f"{ch} does not occur in string '{N}'")
else:
    print(f"{ch} occurs in string '{N}' '{answer1}' times in total.")
