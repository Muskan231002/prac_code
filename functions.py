"""#func
def cal(a,b):
    mean=(a*b)/(a+b)
    print(mean)

a=int(input("Enter no 1"))
b=int(input("Enter no 2"))
cal(a,b)
"""
def avg(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    m=sum/len(numbers)
    return m    
    '''print(sum)    
    print('The avg of these number are',sum/len(numbers))'''
    
p=avg(15,2,30)
print(p)