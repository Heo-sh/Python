#신호등 문제 빨간불: 1 주황불: 2 초록불을: 3
#사용자한테 신호를 받아서 1이면 빨간불입니다,
#2면 주황불입니다,3이면 초로불입니다.
# 그 외의 것들 이라면 잘못입력하셨습니다. 라고 출력해주세요.

a=int(input('신호를 입력하세요(1:빨간불, 2:주황불, 3:초록불): '))

if a==1:
    print('빨간불 입니다.')
elif a==2:
    print('주황불 입니다.')
elif a == 3:
    print('초록불 입니다.')
else:
    print('잘못 입력하셨습니다.')


#임의의 정수를 입력받은 뒤 해당 값이 3의 배수인지 아닌지를 판별하는 프로그램을
#구현하세요.

b= int(input('정수를 입력하세요: '))

if b % 3 == 0:
    print('%d는 3의 배수 입니다' %b)
else:
    print('%d는 3의 배수가 아닙니다' %b)


