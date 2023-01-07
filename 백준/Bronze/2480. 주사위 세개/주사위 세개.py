num1, num2, num3 = map(int, input().split())
result = 0
if num1==num2 and num2 == num3:
    result = 10000+(num1*1000)
    print(result)
elif num1 == num2 or num2 == num3:
    result = 1000+(num2)*100
    print(result)
elif num1 == num3:
    result = 1000+(num3)*100
    print(result)
elif num1 != num2 and num2!=num3:
    result = max(num1, num2, num3) * 100
    print(result)