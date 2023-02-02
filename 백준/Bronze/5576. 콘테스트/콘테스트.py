w = []
k = []
for i in range(1, 21):
    score = int(input())
    if i <11:
        w.append(score)
    else:
        k.append(score)

w.sort(reverse=True)
k.sort(reverse=True)
print((w[0]+w[1]+w[2]),(k[0]+k[1]+k[2]))