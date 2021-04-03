h,b,c,s = map(int,input().split())
result = round((h*b*c*s)/8/1024/1024,1)
print("{0} MB".format(result))