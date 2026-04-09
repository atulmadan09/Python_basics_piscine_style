def ft_count_vandc(string):
    count_v = 0
    count_c = 0
    for i in string:
        if ((ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122)):
            if (ord(i) == 97 or ord(i) == 101 or
                ord(i) == 105 or ord(i) == 111 or
                ord(i) == 117 or ord(i) == 65 or
                ord(i) == 69 or ord(i) == 73 or
                ord(i) == 79 or ord(i) == 85):
                count_v = count_v + 1
            else:
                count_c = count_c + 1
    return count_v, count_c

N = "ATULatul  !"
answer1, answer2 = ft_count_vandc(N)
print(f"The number of vowels are {answer1}")
print(f"The number of consonants are {answer2}")

# def ft_count_vandc(string):
#     count_v = 0
#     count_c = 0

#     for c in string:
#         if c.isalpha():
#             if c.lower() in "aeiou":
#                 count_v += 1
#             else:
#                 count_c += 1

#     return count_v, count_c
