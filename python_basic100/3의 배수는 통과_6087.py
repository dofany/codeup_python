a = int(input())
for i in range(1,a+1):
    if i % 3 == 0:
        print(end='')
        continue
    print(i,end=' ')