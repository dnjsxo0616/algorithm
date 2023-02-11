a, b = input().split()

re_a = a[::-1]
re_b = ''.join(reversed(b))

if re_a > re_b:
    print(re_a)
else:
    print(re_b)