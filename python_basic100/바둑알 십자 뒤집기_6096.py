d = [[]*19 for _ in range(19)]
for i in range(19):
   d[i]=(list(map(int,input().split())))

a = int(input())
for i in range(a):
    b, c = map(int, input().split())

    for j in range(19):
        if d[j][c-1] == 0:
            d[j][c-1] = 1
        else:
            d[j][c-1] = 0
    for j in range(19):
        if d[b-1][j] == 0:
            d[b-1][j] = 1
        else:
            d[b-1][j] = 0

for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()


