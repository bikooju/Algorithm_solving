def solution(s):
    s_stack = []
    
    for char in s:
        if char == "(":
            s_stack.append("(")
        else: # ")"
            if not s_stack: #스택이 비어있으면 바로 False 반환
                return False
            s_stack.pop() #스택에서 짝이 맞는 괄호 제거(가장 마지막에 추가한 "(" 임)
    return len(s_stack) == 0
        