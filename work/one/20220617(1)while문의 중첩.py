#총 5일동안 하루에 3시간씩 수업을 한다.

day = 1 # <- day라는 변수

while day <= 5: #<- 일수 while 조건식 : 일수가 5보다 작거나 같다.
    hour = 1 # <- 교시
    while hour <=3: # <- while 조건식 : 교시가 3보다 작거나 같다.
        print('%d일 차 %d교시입니다.'%(day, hour))
        hour += 1 # <- 시간에 하나씩 더해준다. 3과 같아질 때까지
    day += 1 # <- 일수에 하나씩 더해간다. 5와 같아질 때까지
