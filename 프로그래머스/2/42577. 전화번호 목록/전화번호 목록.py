def solution(phone_book):
    dt = {}
    #전화번호 목록을 해시 테이블에 저장
    for number in phone_book:
        dt[number] = 1
        
    #각 전화번호의 접두사가 해시테이블에 있는지 확인
    for number in phone_book:
        temp = "" #접두사를 하나씩 만들어가는 변수
        for digit in number:
            temp += digit
            if temp in dt and temp != number: #자기 자신을 접두사로 판단하지 않도록
                return False
    return True
        
        
    