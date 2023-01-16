result = 0

for j in range(5):
    score = int(input())
    if score >= 40:
        result += score
    else:
        result += 40
ans = result/5
print(int(ans))