#카페1.py

print('******Hello Cafe******')
print('1.주문하기')
print('2.취소하기')
print('3.결제하기')
print('4.끝내기')

sc = int(input('선택 : '))

if sc == 1:
    print('----주문하기----')
    print('****Menu****')
    print('1.아메리카노\t3800원')
    print('2.카페라떼\t4200원')
    print('3.아이스티\t4500원')
    print('4.돌체라떼\t5200원')
    print('5.버블티\t6100원')
    print('************')
elif sc == 2:
    print('----취소하기----')
elif sc == 3:
    print('----결제하기----')
elif sc == 4:
    print('----끝내기----')
else:
    print('잘못 입력하셨습니다.')
#이 문제 하나로 어느 정도 프로그램이 어떻게 돌아가는 지 알아갈 수 있는 것 같다.
