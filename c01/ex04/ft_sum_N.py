def ft_sum_N(N):
    result = 0
    for i in range (1, N+1):
        result = result + i
    return result

N = 180
answer = ft_sum_N(N)
print(f"The sum till {N} is {answer}")