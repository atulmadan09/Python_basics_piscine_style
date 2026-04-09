def ft_strlen(string):
    length =0
    for i in string:
        length = length + 1
    return length

def ft_str_rev(string):
    answer = ft_strlen(string)
    dest = ""
    i = answer -1
    while (i >= 0):
        dest = dest + string[i] 
        i = i-1
    return dest

N = "Atulrocks  DDD!"
answer = ft_str_rev(N)
print(f"The reversed string is {answer}")