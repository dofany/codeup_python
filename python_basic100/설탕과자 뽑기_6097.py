h,w = map(int,input().split())
n = int(input())
lst = []
for i in range(h):
    lst.append([])
    for j in range(w):
        lst[i].append(0)

for i in range(n):
    l,d,x,y = map(int,input().split())
    if d == 0:
        for j in range(l):
            lst[x-1][y-1+j]=1
    else:
        for j in range(l):
            lst[x-1+j][y-1]=1

for i in range(h):
    for j in range(w):
        print(lst[i][j], end=' ')
    print()