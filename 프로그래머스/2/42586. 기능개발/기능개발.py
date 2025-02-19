def solution(progresses, speeds):
    #주의 : 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포(먼저 배포 될 수 없음)
    #progresses : 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열
    #speeds : 각 작업의 개발 속도가 적힌 정수 배열
    #각 배포마다 몇 개의 기능이 배포되는지 return
    day = 0
    cnt = 0 #완료된 기능 수
    answer = []
    
    while(len(progresses) > 0):
        if(progresses[0] + day*speeds[0] >= 100):
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1 #완료된 기능 추가
        else:
            #완료된 기능이 있을 경우 answer에 추가해주고 0으로 초기화
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            else:
                day += 1 #완료된 기능이 없으므로 완료될 때까지 날짜 올려주기
    answer.append(cnt) #progresses이 이제 빈배열일 경우도 고려해서 마지막 남은 cnt 추가
    return answer
    
        
        
    