r = int(input("Enter the number of rows: "))

for i in range(1, r + 1):
    print(" " * (r - i), end="")

    for j in range(1, 2 * i):
        if i == r or j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()
