def ft_strlen(string):
    length = 0
    for i in string:
        length = length + 1
    return length

def ft_compare_two_strings(string1, string2):
    answer1 = ft_strlen(string1)
    answer2 = ft_strlen(string2)
    # count = 0
    # for i in range(0, answer):
    if (string1 == string2):
        return 1
    return 0

N1 = input("Please input the string1: ")
N2 = input("Please input the string2: ")

answer1 = ft_compare_two_strings(N1, N2)
if answer1 == 1:
    print("The two strings are same.")
else:
    print("The two strings are not same.")
