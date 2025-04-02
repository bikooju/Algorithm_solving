import sys

T = int(sys.stdin.readline().rstrip())

answer = []

for i in range(T):
    
    N = sys.stdin.readline().rstrip()
    
    cnt = 0 #왼쪽 느낌표 개수(반전)
    idx = 0 #인덱스(포인터)
    fact = 0 #오른쪽 느낌표 개수(팩토리얼)
    
    #왼쪽 느낌표 개수 카운트
    while len(N) > idx and N[idx] == "!":
        cnt += 1
        idx += 1 #다음 인덱스를 가리킴
    
    
    number = int(N[idx])
    idx += 1 #현재 위치가 숫자이므로 다음 인덱스로 오른쪽 느낌표를 가리키게한다
    
    #오른쪽 느낌표 개수 카운트
    while len(N) > idx and N[idx] == "!":
        fact += 1
        idx += 1
    
    #팩토리얼 먼저 적용
    if fact >= 1:
        number = 1
        
    #후에 반전 적용
    for i in range(cnt):
        if number == 1:
            number = 0
        else:
            number = 1
    
    answer.append(number)
    
    
for a in answer:
    print(a)
        
    
        
    
    