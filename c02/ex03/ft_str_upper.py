def ft_str_upper(string):
    dest = ""
    for i in string:
        if (ord(i) >= 97 and ord(i) <= 122):
            dest = dest + chr(ord(i)- 32)
        else:
            dest = dest + i 
    return dest

N = "Atulrocks  DDD!"
answer = ft_str_upper(N)
print(f"The uppercased string is {answer}")