import sys

N, M = list(map(int, sys.stdin.readline().split()))
card_list = list(map(int, sys.stdin.readline().split()))
sum_list = []

for i in range(len(card_list)):
    for j in range(i + 1, len(card_list) - 1):
        for k in range(j + 1, len(card_list)):
            if card_list[i] + card_list[j] + card_list[k] > M:
                continue
            else:
                sum_list.append(card_list[i] + card_list[j] + card_list[k])

print(max(sum_list))
