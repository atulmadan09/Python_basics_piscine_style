# def ft_strlen(string):
#     length = 0
#     for i in string:
#         length = length + 1
#     return length

# def ft_str_first_occ(string):
#     length = ft_strlen(string)
#     for i in range(length):
#         if ( string[i] == 'A' ):
#             return i
#     return -1

# N = "A!dfgaTULfLUT!"
# answer1 = ft_str_first_occ(N)
# if (answer1 == -1):
#     print(f"A does not occur in String {N}")
# else:
#     print(f"A occurs in String {N} at {answer1+1}th position")

def ft_strlen(string):
    length = 0
    for i in string:
        length += 1
    return length


def ft_str_first_occ(string, target):
    length = ft_strlen(string)
    for i in range(length):
        if string[i] == target:
            return i
    return -1


# 🔹 Take input from user
N = input("Enter a string: ")
ch = input("Enter a character to search: ")

answer1 = ft_str_first_occ(N, ch)

if answer1 == -1:
    print(f"{ch} does not occur in string '{N}'")
else:
    print(f"{ch} occurs in string '{N}' at position {answer1 + 1}")