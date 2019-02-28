from random import shuffle

tags = []
orientation = []

with open("d_pet_pictures.txt") as f:
    N = int(f.readline().strip())
    for i in range(N):
        x = f.readline().strip().split()
        orientation.append(x[0])
        s = set()
        tags.append([i, set([i for i in x[2:]])])

ver = []


arr = [str(i) for i in range(N)]
shuffle(arr)
print(len([i for i in orientation if i == 'H']))
print(len([i for i in orientation if i == 'V']))
n = len([i for i in orientation if i == 'H']) + len([i for i in orientation if i == 'V'])//2
out = open("output.txt", "w")
out.write(str(n)+"\n")
for i in range(N):
    if orientation[int(arr[i])] == 'V':
        if len(ver) == 1:
            out.write(arr[i]+" "+ver[0]+"\n")
            ver = []
        else:
            ver.append(arr[i])
            
    else:
        out.write(arr[i]+"\n")
out.close()
