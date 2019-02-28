
tags = []
orientation = []

with open("b_lovely_landscapes.txt") as f:
    N = int(f.readline().strip())
    for i in range(N):
        x = f.readline().strip().split()
        orientation.append(x[0])
        s = set()
        tags.append([i, set([i for i in x[2:]])])
