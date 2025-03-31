import sys
N = int(sys.stdin.readline().rstrip())
#문자열 비교는 기준 잡기(첫번쨰 단어 => 비교기준)
#나머지 단어를 첫번째 단어와 비교
first_word = list(sys.stdin.readline().rstrip())

for i in range(N-1):
    other_word = list(sys.stdin.readline().rstrip())
    for j in range(len(first_word)):
        if first_word[j] != other_word[j]:
            first_word[j] = '?' #갱신

print(''.join(first_word)) #리스트 -> 문자열

