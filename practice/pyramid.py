r=int(input("Enter the number of row"))
for i in range(1,r+1):
    for j in range(i,r+1):
        print(" ",end="")
    for k in range (1,i+1):
        if k == 1 or k == i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(r-1,0,-1):
    for j in range(i,r+1):
        print(" ",end="")
    for k in range (1,i+1):
        if k == 1 or k == i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
