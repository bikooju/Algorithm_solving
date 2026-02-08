import sys
T = int(sys.stdin.readline())
ps_list = [sys.stdin.readline() for _ in range(T)]
for ps in ps_list: # ps : (())())
    is_vps = True
    count = 0
    for s in ps: # s -> "("
        if s == '(':
            count += 1
        elif s == ')':
            if count > 0:
                count -= 1
            else:
                is_vps = False
                break


    if count != 0:
        is_vps = False

    if is_vps:
        print("YES")
    else:
        print("NO")