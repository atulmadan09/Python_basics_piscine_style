def ft_fibonacci(N):
    result = 0
    if (N < 0):
        result = -1
    elif (N == 0):
        result = 0
    elif (N == 1 or N == 2):
        result = 1
    else:
        result = ft_fibonacci(N-1) + ft_fibonacci(N-2) 
    return result

N = -15
answer = ft_fibonacci(N)
print(f"The fibonacci of {N} is {answer}")