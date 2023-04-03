num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

sum_num1 = sum(num1)
sum_num2 = sum(num2)

if sum_num1 >= sum_num2:
    print(sum_num1)
elif sum_num1 < sum_num2:
    print(sum_num2)