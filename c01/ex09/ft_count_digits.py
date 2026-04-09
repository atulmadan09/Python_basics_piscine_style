def ft_count_digits(N):
    count = 0
    while (N > 0):
        count = count + 1
        N = N // 10
    return count

N = 126567621
answer = ft_count_digits(N)
print(f"The number of digits of {N} is {answer}")
