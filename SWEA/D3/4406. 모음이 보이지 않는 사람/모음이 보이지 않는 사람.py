arr = 'aeiou'

T = int(input())
for t in range(1, T+1):
    word = input()
    for i in range(len(arr)):
        word = word.replace(arr[i], '')
    print(f'#{t} {word}')