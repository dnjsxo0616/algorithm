T = int(input())

for t in range(1, T+1):
    a, b = list(map(int, input().split()))
    result = a//b
    result1 = a%b
    print(f"#{t} {result} {result1}")