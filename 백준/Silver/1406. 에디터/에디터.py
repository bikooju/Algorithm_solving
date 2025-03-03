import sys

st1 = list(sys.stdin.readline().rstrip())  # 왼쪽 스택
st2 = []  # 오른쪽 스택

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()  # 입력 명령

    if command[0] == 'L':  # 커서를 왼쪽으로 이동
        if st1:
            st2.append(st1.pop())

    elif command[0] == 'D':  # 커서를 오른쪽으로 이동
        if st2:
            st1.append(st2.pop())

    elif command[0] == 'B':  # 커서 왼쪽 문자 삭제
        if st1:
            st1.pop()

    else:  # 문자 삽입 (command[0] == 'P')
        st1.append(command[1])

st1.extend(reversed(st2))  # 오른쪽 스택에 남은 문자들을 다시 붙이기
print(''.join(st1))  # 최종 문자열 출력
