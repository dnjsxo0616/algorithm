T = int(input())


for t in range(T):
    score = list(map(int, input().split()))
    cnt = 0
    score.remove(score[0])
    sc_avg = (sum(score)/len(score))
    
    for i in score:
        if i > sc_avg:
            cnt += 1
    ans = cnt/len(score)*100
    print(f'{ans:.3f}%')