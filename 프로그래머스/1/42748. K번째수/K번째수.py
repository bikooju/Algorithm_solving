def solution(array, commands):
    answer = []
    lst = []
    i = 0
    while i < len(commands):
        lst = []
        start = commands[i][0]
        end = commands[i][1]
        k = commands[i][2]
        for j in range(start-1,end):
            lst.append(array[j])
        lst.sort()
        answer.append(lst[k-1]) #인덱스 기준으로(k번째이니까 -> k-1 인덱스)
        i += 1
    return answer