ans = ['' for _ in range(13)] #ans[i] => 입력 i일때의 답(문자열)
ans[0] = '-' 

for i in range(1,13):
    ans[i] = ans[i-1] + ' ' * (3**(i-1)) + ans[i-1]

while True:
    try:
        N = int(input())
        print(ans[N])
    except:
        break