def ft_comb_1():
    for i in range (0, 10):
        for j in range (i+1, 10):
            if (i != j ):
                print(f"{i}{j}", end= ' ')

ft_comb_1()