# using Loops
n=int(input("Enter a number:"))
rev=0
while n>0:
    a=n%10
    rev=rev*10+a
    n=n//10
print(rev)

# using slicing
n=int(input("Enter a number:"))
print(str(n)[::-1])


