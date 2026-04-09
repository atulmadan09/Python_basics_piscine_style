def ft_num_rev(N):
    print (N%10, end='')
    if (N > 9):
        ft_num_rev(N//10)

N = 100
ft_num_rev(N)
# print(f"The reverse of {N} is {answer}")