ns = input()
n = int(ns)
con = 0 
while True:
    a = int((n%10)) # 6
    b= int((n/10 + n%10)) # 8
    ans = (a * 10) + (b%10) # 68
    con += 1
    if str(ans) == ns:
        break
    else:
        n = ans
print(con)
