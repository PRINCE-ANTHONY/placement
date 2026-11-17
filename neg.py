n = int(input())
answer = None

for i in range(n):
    number = int(input())
    # Stop when the first negative number is found
    if number < 0:
        answer = number
        break

print(answer)