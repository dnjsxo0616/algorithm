A = int(input())
B = int(input())
C = int(input())

if (A+B+C) == 180:
    if A==B and A != C:
        print('Isosceles')
    elif A==C and B != C:
        print('Isosceles')
    elif B==C and A != B:
        print('Isosceles')
    elif A != B and A != C and B != C:
        print('Scalene')
    elif A == 60 and B == 60 and C == 60:
        print('Equilateral')
else:
    print('Error')