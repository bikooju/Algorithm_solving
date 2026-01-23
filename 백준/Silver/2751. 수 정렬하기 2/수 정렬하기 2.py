import sys
N = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for _ in range(N)]
n_list.sort()
sys.stdout.write('\n'.join(map(str, n_list)))