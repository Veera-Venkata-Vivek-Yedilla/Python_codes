n=int(input("enter a number:"))
if n==1:
    print('not a prime number')
elif n>1:
    for i in range(2,n):
        if n%i==0:
            print("not a prime number")
            break
    else:
        print("prime number")