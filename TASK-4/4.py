n=int(input("Enter number:\n"))
num=n
reci=0
while(n>0):
    once=n%10
    reci=reci*10+once
    n=n//10
if(num==reci):
    print("TRUE")
else:
    print("FALSE")
