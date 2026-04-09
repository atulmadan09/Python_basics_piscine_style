def ft_strcmp(string1, string2):
    if (len(string1) == len(string2)):
        for i in range(0, len(string1)):
            if (string1[i] != string2[i]):
                return(ord(string1[i]) - ord(string2[i]))
    
    else:
        for i in range(0, min(len(string1), len(string2))):
            if (string1[i] != string2[i]):
                return(ord(string1[i]) - ord(string2[i]))
        return (len(string1) - len(string2))
    return 0

N1 = input("Please input the string1: ")
N2 = input("Please input the string2: ")

answer1 = ft_strcmp(N1, N2)
if answer1 != 0:
    print(f"The two strings are different with a value of {answer1}.")
else:
    print("The two strings are same.")
