import sys

#소문자, 대문자, 숫자, 공백의 개수
while True:
    N = sys.stdin.readline().rstrip('\n')
    if not N:
        break
    
    s_count = 0
    S_count = 0
    number_count = 0
    space_count = 0
    
    for ch in N:
        if ch.islower():
            s_count += 1
        elif ch.isupper():
            S_count += 1
        elif ch.isdigit():
            number_count += 1
        elif ch.isspace():
            space_count += 1
    
    print(s_count, S_count, number_count, space_count)
          
        