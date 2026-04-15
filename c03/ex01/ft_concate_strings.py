def ft_concate_strings(string1, string2):
    string1 = string1 + ' '
    # for i in range(0, len(string2)):
    #     string1 = string1 + string2[i]
    return string1 + string2

N1 = input("Please input the string1: ")
N2 = input("Please input the string2: ")

answer1 = ft_concate_strings(N1,N2)
print(f"The two strings are '{answer1}'")