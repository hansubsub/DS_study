def solution(diffs, times, limit):
    level=1 #난이도
    
    while True: # 계속 시간 오바하다가 이제 오바 안하면 리턴
        total=0
        for i in range(len(diffs)):  #숙련도 i 인경우 i=0~퍼즐 수
            if diffs[i]<=level:
                total+=times[i]
            else:
                #if==0을 밖으로 꺼낸게 문제였다.조건의 우선순위를 잘 따지자!
                if i==0:
                    t=times[i]+(diffs[i]-level)*times[i]
                else:
                    t= times[i]+(diffs[i]-level)*(times[i]+times[i-1])
                total+=t
        #숙련도 level 일때 시간 구하기 완 -> 다음레벨로 넘어감, total,t 초기화, 레벨업  !넘어가기 전에 확인하기
        if total<=limit:
            break
        level+=1
    return level
