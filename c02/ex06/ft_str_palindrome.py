def ft_strlen(string):
    length =0
    for i in string:
        length = length + 1
    return length

# def ft_str_rev(string):
#     answer = ft_strlen(string)
#     dest = ""
#     i = answer -1
#     while (i >= 0):
#         dest = dest + string[i] 
#         i = i-1
#     return dest

# def ft_str_palindrome(string):
#     answer = ft_str_rev(string)
#     if (string == answer):
#         return 1
#     return 0;

def ft_str_palindrome(string):
    answer = ft_strlen(string)
    for i in range ( 0, answer//2):
        if (string[i] != string[answer-1-i]):
            return 0
    return 1

N = "!ATULfLUTA!"
answer1 = ft_str_palindrome(N)
if (answer1 == 1):
    print(f"String {N} is a palindrome")
else:
    print(f"String {N} is not a palindrome")

