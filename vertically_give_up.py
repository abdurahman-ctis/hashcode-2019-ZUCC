from random import shuffle

with open("b_lovely_landscapes.txt") as f:
    N = int(f.readline().strip())


arr = [str(i) for i in range(N)]
shuffle(arr)

out = open("output.txt", "w")
out.write(str(N//2)+"\n")
for i in range(1, N, 2):
    out.write(arr[i]+" "+arr[i-1]+"\n")
out.close()
