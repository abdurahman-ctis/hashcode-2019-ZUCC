from random import shuffle

with open("b_lovely_landscapes.txt") as f:
    N = int(f.readline().strip())


arr = [str(i) for i in range(N)]
shuffle(arr)

out = open("output.txt", "w")
out.write(str(N)+"\n")
out.write("\n".join(arr))
