def ft_factorial(N):
    result = 1
    for i in range (1, N+1):
        result = result * i
    return result

N = 5
answer = ft_factorial(N)
print(f"The factorial of {N} is {answer}")