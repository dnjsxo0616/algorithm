total_x = []
total_y = []
# 리스트를 순회하는 range(3)
for i in range(3):
    x, y = list(map(int, input().split()))
    # x 값 저장하는 리스트
    total_x.append(x)
    # y 값 저장하는 리스트
    total_y.append(y)

# x리스트에서 1개 남은 것
for j in total_x:
  if total_x.count(j) == 1:
    res_x = j
 # y리스트에서 1개 남은 것
for k in total_y:
  if total_y.count(k) == 1:
    res_y = k
print(res_x, res_y)