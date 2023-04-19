#신호등 문제 - 빨간불 : 1, 주황불 : 2, 초록불을 : 3
#사용자에게 신호를 받아서 1이면 빨간불입니다.
#2이면 주황불, 3이면 초록불
#그 이외는 잘못 입력하셨습니다. 출력하라
color = int(input('신호를 정수로 입력해주세요. >>>'))

if color ==1:
    print('빨간불')
elif color ==2:
    print('주황불')
elif color ==3:
    print('초록불')
else:
    print('잘못 입력하셨습니다.')
#ex_traffic.py
