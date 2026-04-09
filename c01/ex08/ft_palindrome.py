def ft_palindrome(N):
    rev = 0
    while (N > 0):
        rev = rev* 10 + N%10
        N = N // 10
    return rev

N = 126621
answer = ft_palindrome(N)
if (N - answer == 0):
    print("Number is a palindrone")
else:
    print("Number is not a palindrome")
