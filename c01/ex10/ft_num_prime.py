def ft_num_prime(N):
    for i in range (2, (N//2 + 1)):
        if ( N % i == 0):
            return 1
    return 0

N = 1055674837
answer = ft_num_prime(N)
if (answer == 1):
    print(f"The number {N} is not a prime")
else:
    print(f"The number {N} is a prime")