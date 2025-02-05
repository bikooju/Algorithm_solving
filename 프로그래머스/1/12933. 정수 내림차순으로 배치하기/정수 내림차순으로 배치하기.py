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


#추가
def solution(n):
    ls = list(str(n))
    ls.sort(reverse=True)
    return int("".join(ls)) // "".join(ls) => 리스트의 요소를 하나의 문자열로 합치기
    
