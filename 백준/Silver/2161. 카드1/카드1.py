card = list(range(1, int(input())+1))
ans = []

while len(card)>1:
    ans.append(card.pop(0))
    card.append(card[0])
    card.pop(0)
print(*ans, *card)