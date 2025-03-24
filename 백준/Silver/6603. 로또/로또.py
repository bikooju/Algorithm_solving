import sys

def combination(index,level):
    if level == 6:
        for u in choose:
            print(u,end=' ')
        print()

    for i in range(index,k):
        choose.append(arr[i])
        combination(i+1, level+1)
        choose.pop()

while True:
    choose = []
    number_k = list(map(int, sys.stdin.readline().split()))

    k = number_k[0]
    arr = number_k[1:]
    if k==0:
        break

    combination(0,0)
    print()
