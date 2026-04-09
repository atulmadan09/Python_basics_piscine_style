def ft_comb_2():
    for i in range (0, 10):
        for j in range (i+1, 10):
            for k in range (j+1, 10):
                if (i != j & j != k ):
                    print(f"{i}{j}{k}", end= ' ')

ft_comb_2()