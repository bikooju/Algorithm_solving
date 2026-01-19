import sys
N = int(sys.stdin.readline())

layer = 1 # 현재 층
end = 1 # 현재 층의 마지막 숫자

while N > end:
    end += 6 * layer
    layer += 1
    
print(layer)