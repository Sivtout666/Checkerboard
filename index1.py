def checkerboard(size):
    for line in range(size):
        for column in range(size):
            cond1 = line % 2 == 0
            cond2 = column %  2 == 0
            if (cond1 and cond2) or (not cond1 and not cond2):
                print("#", end="")
            else:
                print(".", end="")
        print()
checkerboard(10)
