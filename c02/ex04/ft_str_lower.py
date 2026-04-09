def ft_str_lower(string):
    dest = ""
    for i in string:
        if (ord(i) >= 65 and ord(i) <= 90):
            dest = dest + chr(ord(i)+ 32)
        else:
            dest = dest + i 
    return dest

N = "Atulrocks  DDD!"
answer = ft_str_lower(N)
print(f"The lowercased string is {answer}")