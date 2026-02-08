import sys
T = int(sys.stdin.readline())
for _ in range(T):
    ps = sys.stdin.readline().rstrip()
    stack = []
    is_vps = True
    for s in ps: # ps : (())())   => s : "("
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
    
    if stack:
        is_vps = False
    
    if is_vps:
        print("YES")
    else:
        print("NO")


