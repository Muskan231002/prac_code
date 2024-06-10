f=open("myfile.txt","r")
i=0
while True:
    i+=1
    line=f.readline()
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"marks of student {i}in maths is {m1}")
    print(f"marks of student {i}in maths is {m2}")
    print(f"marks of student {i}in maths is {m3}")

    if not line:
        break
#-----------------------------------------------------------
   #type casting  m1=line.split(",")[0]
    #m2=int(line.split(","))[1]
    #m3=int(line.split(","))[2]

