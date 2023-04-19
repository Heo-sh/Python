a = int(input('0~100까지의 숫자를 적으세요. >>>'))
if a>=80:
    print('합격입니다.')
else:
    print('불합격입니다')
#p.99 1번 응용문제 학점 프로그램
s = int(input('점수를 입력하세요. >>> ')) #elif문에 >=(크거나 같다),형식 지정자를 같이 활용
if s >= 90:
    print('점수는 %d이고, 학점은 A학점입니다.'%s)
elif s >= 80:
    print('점수는 %d이고, 학점은 B학점입니다.'%s) 
elif s >= 70:
    print('점수는 %d이고, 학점은 C학점입니다.'%s)
elif s >= 60:
    print('점수는 %d이고, 학점은 D학점입니다.'%s)
else:
    print('점수는 %d이고, 학점은 F학점입니다.'%s)
#p.99번 2번 응용문제 3의 배수
t = int(input('정수를 입력하세요. >>> '))
if t % 3 == 0: # %(나눈 수의 나머지)를 이용 
    print('%d는 3의 배수입니다.'%t)
else:
    print('%d는 3의 배수가 아닙니다.'%t)
#p.99 3번 응용문제 가장 큰 수
c = int(input('정수 1 입력 >>> '))
d = int(input('정수 2 입력 >>> '))
e = int(input('정수 3 입력 >>> '))

if c>d and c>e: #and를 이용하여 해결
    print('가장 큰 수는 %d입니다.'%c)
elif d>c and d>e:
    print('가장 큰 수는 %d입니다.'%d)
elif e>c and e>d:
    print('가장 큰 수는 %d입니다.'%e)
#p.99 4번 응용문제 차량번호
car = input("차량번호를 입력하세요. 단, 차량번호는 '111가1111입니다.'>>>")
     #문자열로 입력 후
if int(car[7]) % 2 == 0: # 정수형으로 변환 후 출력
    print('차량번호 \'%s\'는 오늘 운행가능입니다.'%car)
else:
    print('차량번호 \'%s\'는 오늘 운행불가입니다.'%car)
                
