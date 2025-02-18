from collections import deque
def solution(arr):
    answer = deque()
    #연속인것들을 answer에 하나씩만 넣기
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
            continue
        if arr[i-1] == arr[i]: #연속
            if answer.pop() == arr[i]: #마지막으로 넣은게 연속된값이면
                answer.append(arr[i])
                continue
        answer.append(arr[i]) #처음 넣음
    return list(answer)