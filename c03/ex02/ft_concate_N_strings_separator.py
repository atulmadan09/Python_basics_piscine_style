def ft_concate_N_strings_separator(string1, string2):
    string1 = string1 + ', '
    return string1 + string2

N1 = input("Please input the string1: ")
N2 = input("Please input the string2: ")
x3 = input("Any more strings?(y/n)")
if (x3 == 'y'):
    input("Please input the string3: ")
if (x3 == 'n'):
    answer1 = ft_concate_N_strings_separator(N1,N2)

print(f"The concatenated strings are {answer1}")