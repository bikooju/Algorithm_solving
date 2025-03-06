import sys
from collections import Counter

name = sys.stdin.readline().rstrip()
checked_words = Counter(name)
cnt = 0
mid = ''
result = '' #앞부분

for k,v in checked_words.items():
    if v % 2 == 1:
        cnt += 1
        mid = k
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()

for k,v in sorted(checked_words.items()):
    result += k*(v // 2)

print(result + mid + result[::-1])