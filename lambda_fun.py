# def appl(fx,value):
#     return 6* fx(value)
# def cube(x):
#     x=3
#     return x*x*x


# print(appl(cube ,2))
#---------------------------------------------
def appl(fx,value):
    return 6+ fx(value)
print(appl(lambda x:x*x*x,2))