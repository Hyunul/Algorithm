n, m = map(int, input().split())

card_list = list(map(int, input().split()))
card_list = sorted(card_list, reverse=True)
result = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if (card_list[i] + card_list[j] + card_list[k]) <= m:
                result.append(card_list[i] + card_list[j] + card_list[k])

result = sorted(result, reverse=True)
print(result[0])