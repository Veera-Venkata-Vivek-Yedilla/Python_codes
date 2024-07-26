n=int(input("Enter a number:"))
m=n
s=0
cube=len(str(n))
while n>0:
    a=n%10
    s=a**cube+s
    n=n//10
print(s)
if m==s:
    print('armstrong')
else:
    print('not a armstrong')