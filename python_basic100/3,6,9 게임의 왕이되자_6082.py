a = int(input())
result = 0
for i in range(1,a+1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print("X",end=' ')
        continue

    print(i, end=' ')
