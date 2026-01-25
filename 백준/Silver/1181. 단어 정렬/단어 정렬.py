import sys
N = int(sys.stdin.readline())
words = set()
for _ in range(N):
    words.add(sys.stdin.readline().rstrip())

result = sorted(words, key=lambda x: (len(x), x))

for word in result:
    print(word)