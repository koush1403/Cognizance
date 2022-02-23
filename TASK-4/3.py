a=int(input("Enter The Number of Students : "))

x=[["Roll","Name","Marks obtained"]]

for i in range(a):

    roll=input("Enter Roll No : ")
    name=input("Enter Student Name : ")
    marks=int(input("Enter Marks obtained : "))

    x.append([roll,name,marks])

for i in range(len(x)):

    for j in range(len(x[i])):

        r=x[i][j]

        print(r,end='\t')

    print('\n')

l=int(input("which row should be displayed : "))

for i in x[l]:
    
    print(i,end='\t')