l=[1,2,3,4,5,6,7,]
newl=list(map(lambda x:x*x*x,l))
print(newl)
filter_func=lambda x: x>4
nl=list(filter(filter_func,l))
print(nl)
from functools import reduce
sum=reduce(lambda x,y:x+y,l)
print(sum)