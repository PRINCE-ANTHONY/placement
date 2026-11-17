n = int(input())
count = 0

for _ in range(n):
    score = int(input())
    if score == -1:
        break
    if not (0 <= score <= 100):
        continue
    count += 1

print(count)

