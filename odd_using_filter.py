def odd(x):
    return x%2==1
a=[2,3,4,5,7,8,10,13,16]
result=filter(odd,a)
print(a)
print(list(result))

        