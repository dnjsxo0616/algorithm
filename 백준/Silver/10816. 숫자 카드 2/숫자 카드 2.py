n = int(input()) # 상근이가 가지고있는 카드수
# 정수M개가 주어질 때 이 수가 적혀있는 숫자 카드를 몇개 가지고 있나
n_list= list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split())) # 있어야할 개수

word = {}
for i in m_list:
    word[i]=0

for j in n_list:
    if j not in word:
        continue
    word[j] += 1

for i in m_list:
    print(word[i], end = ' ')
