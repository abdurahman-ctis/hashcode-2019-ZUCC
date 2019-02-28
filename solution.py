def find_min(x1, x2):
    return  max(len(x1), len(x2)) - len(x1.intersection(x2))
    #return min(len(x1.intersection(x2)), min(len(x1.difference(x2)),len(x2.difference(x1))))



tags = []
orientation = []

with open("b_lovely_landscapes.txt") as f:
    N = int(f.readline().strip())
    for i in range(N):
        x = f.readline().strip().split()
        orientation.append(x[0])
        s = set()
        tags.append([i, set([i for i in x[2:]])])


tags = sorted(tags, reverse=True, key=lambda x: len(x[1]))
res = []
n = N

# for i in range(len(tags)):
#     maxi, maxj = -1, -1
#     imax = 0
#     for j in range( i + 1 , len(tags)):
#         temp = find_min(tags[i][1], tags[j][1])
#         if temp > imax:
#             maxi, maxj = i, j
i = 0
while n>1:
    maxi, maxj = -1, -1
    imax = -1
    for j in range(n):
        if abs(len(tags[i][1]) - len(tags[j][1])) < 10:
            break 
        if j != i:
            temp = find_min(tags[i][1], tags[j][1])
            if temp > imax:
                maxi, maxj = i, j
                imax = temp
    res.append(str(tags.pop(maxi)[0]))
    #res.append(str(tags.pop(maxj)[0]))
    i = maxj
    n -= 1
    print(n)

out = open("output.txt", "w")
out.write(str(len(res))+"\n")
out.write('\n'.join(res))
# s = []
# s.append()
# v = []
# for i in range(N):
#     if orientation[i] == 'H':
#         out.write(str(i))
#         out.write("\n")
#     else:
#         if len(v) == 2:
#             out.write(str(v[0])+" "+str(v[1]))
#             out.write("\n")
#         else:
#             v.append(i)

# if len(v) == 2:
#     out.write(str(v[0])+" "+str(v[1]))
#     out.write("\n")

out.close()

