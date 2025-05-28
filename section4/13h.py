#to print prime nums frm 1-101 

n=2
count=1
while (count<=101):
    count=count+1
    for i in range (2,n+1,1):
        if (n%i==0):
            print("Not a prime number")
        else:
            print(n," is prime")
    n=n+1
    