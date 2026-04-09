def ft_strlen(string):
    length =0
    # while (i < len(string)):
    for i in string:
        length = length + 1
    return length

N = "Atulrocks  DDD!"
answer = ft_strlen(N)
print(f"The length of string is {answer}")
