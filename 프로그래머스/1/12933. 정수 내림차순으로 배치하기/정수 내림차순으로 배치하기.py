def solution(n):
    answer = 0
    s = ""
    list_answer = []
    for i in str(n):
        list_answer.append(int(i))
    list_answer.sort()
    list_answer.reverse()
    
    for i in list_answer:
        s += str(i)
    answer = int(s)
    return answer