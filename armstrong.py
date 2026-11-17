n=int(input("Enter the number of elements in the list: "))
l=len(str(n))
A=0
b=0
temp=n
while n!=0:
    b=(n%10)
    A=A+b**l
    n=n//10
print(A)
if temp==A:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")
    