def cube(x):
    return x*x*x

l=[1,2,3,4,5]
newl=[]
for item in l:
    cubes=cube(item)
    newl.append(cubes)
print(newl)    