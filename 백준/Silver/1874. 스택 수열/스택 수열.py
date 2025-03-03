import sys

count = 1
stack = [] #오름차순으로 숫자를 넣는 스택
temp = True
op = [] #push,pop 여부에 따른 연산 여부를 +,-로 저장

n = int(sys.stdin.readline())
for _ in range(n):
	num = int(sys.stdin.readline())
	# num이하 숫자까지 스택에 넣기
	while count <= num:
		stack.append(count) 
		op.append('+')
		count += 1

	#num이랑 스택 맨 위 숫자가 동일하다면 제거
	if stack[-1] == num:
		stack.pop()
		op.append('-')
	#스택 수열을 만들 수 없으므로 NO
	else:
		temp = False
		break
# 스택 수열을 만들 수 있는지 여부에 따라 출력
if temp == False:
	print("NO")
else:
	for i in op:
		print(i)

