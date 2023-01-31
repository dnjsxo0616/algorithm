cnt = 0
dict_lis = {}
for _ in range(10):
    num = int(input())
    cnt += num
    if num in dict_lis:
        dict_lis[num] += 1
    else:
        dict_lis[num] = 1

dict_avg = int(cnt/10)
dict_max = max(dict_lis, key=dict_lis.get) # max(dict_lis) -> dict_lis의 key값 중 최대값 / Key = dict_lis.get에서 dict_list.get은 일반적으로 dict_lis.get(key)와 같이쓰여 key에 대한 value 출력
# dict_max = [k for k, v in dict_lis.items() if max(dict_lis.values()) == v] # 리스트로 나옴 k에 key의 값이 v에 value값이 반복되며 v가 value 중 최대값일 때 k출력
print(dict_avg)
print(dict_max)