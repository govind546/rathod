import functools
lis=[3,5,6,7,8]
print("the sum of elements",end="")
print(functools.reduce(lambda a,b:a+b,lis))