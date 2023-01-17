N = int(input())


numbers = list(map(int, input().split()))
a=sorted(numbers)
numbers.sort(reverse=True)
print(a[0], numbers[0])