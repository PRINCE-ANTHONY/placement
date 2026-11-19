n=input()
h=""
o=""
for i in n:
    if i == "#":
        h+=i
    else:
        o+=i
print(h+o)