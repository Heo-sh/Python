#1번 응용문제
#5자리로 구성된 학번 31025를 학년, 반, 번호로
#나눠 출력하는 프로그램을 구현하라
''' 3학년 10반 25번'''

classnumber = [3,10,25]

print('3학년 10반 25번')
print(classnumber[0],'학년', classnumber[1],'반', classnumber[2],'번')

#2번 응용문제
#전체 차량번호에서 뒤에 숫자 4자리만 출력하는 프로그램을 구현하세요.
#전체 차량번호는 '서울2가1234'
#                '10가1234'
#                '288가1234'와 같이 다르지만,
#모두 차량번호 4자리는 '1234'입니다.

car = ['서','울',2,'가',1,2,3,4]
car2 = [1,0,'가',1,2,3,4]
car3 = [2,8,8,'가',1,2,3,4]

print(car,'의 차량번호 4자리는',car[-4:],'입니다')

C = '서울2가1234'
print('서울2가1234의 차량번호 4자리는',C[-4:],'입니다.')

#5번 응용문제
#어떤 중국음식점의 이번 주말 할인 메뉴는 금요일은 탕수육,
#토요일은 유산슬, 일요일은 팔보채입니다.
#요일별 할인 메뉴를 딕셔너리(dict) 구조로 저장하고
#다음과 같이 출력하는 프로그램을 구현하시오.

chinese = {
    '금요일' : '탕수육',
    '토요일' : '유산슬',
    '일요일' : '팔보채'
    }
for word in chinese:
    print('%s : %s'%(word,chinese.get(word)))
