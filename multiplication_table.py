print("  1 2 3 4 5 6 7 8 9 10\n")
for i in range (1, 11):
    for j in range (0, 11):
        if j == 0:
            print(i * 1, end = " ")
        else:
            p = i * j
            print(p, end = " ")
    print("\n")