d = [[] * 10 for _ in range(10)]
for i in range(10):
    d[i] = (list(map(int, input().split())))

x = 1
y = 1
while (x < 10 and y < 10):
    if d[1][1] == 2:
        d[1][1] = 9
        break
    else:
        d[1][1] = 9

    if (x < 10) and (y + 1 < 10) and (d[x][y + 1] == 0):
        d[x][y + 1] = 9
        y += 1
    elif (x < 10) and (y + 1 < 10) and (d[x][y + 1] == 2):
        d[x][y + 1] = 9
        break
    elif (x + 1 < 10) and (y < 10) and (d[x + 1][y] == 0):
        d[x + 1][y] = 9
        x += 1
    elif (x + 1 < 10) and (y < 10) and (d[x + 1][y] == 2):
        d[x + 1][y] = 9
        break
    else:
        break

for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()
