def ft_strlen(string):
    length = 0
    for i in string:
        length = length + 1
    return length


def ft_str_last_occ(string, target):
    length = ft_strlen(string)
    for i in range(length - 1, -1, -1):
        if (string[i] == target):
            return i
    return -1


# 🔹 Take input from user
N = input("Enter a string: ")
ch = input("Enter a character to search: ")

answer1 = ft_str_last_occ(N, ch)

if answer1 == -1:
    print(f"{ch} does not occur in string '{N}'")
else:
    print(f"The last {ch} occurs in string '{N}' at position {answer1 + 1}")