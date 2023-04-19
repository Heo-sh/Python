#총 5일동안 하루에 3시간씩 수업을 한다.

day = 1

while day <= 5:
    hour = 1
    while hour <=3:
        print('%d일차 %d교시입니다.'%(day,hour))
        hour +=1
    day += 1
