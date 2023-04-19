#p.85 응용 예제 1번 임의의 두자리 정수 구하라
a = int(input('10~99 사이의 정수를 입력하세요 >>>'))
b = a//10 # //는 나눈 값의 몫이 나오게 한다.
c = a % 10 # %는 나눈 값의 나머지가 나오게 한다.
print('십의 자리 : %d'%b)
print('일의 자리 : %d'%c)
#p.85 응용 예제 2번 시간 변환
sec = int(input('초를 입력하세요 >>> '))

hour = sec//3600
minute = hour%60
se = sec%60

print('변환 결과는 %d시간 %d분 %d초입니다.'%(hour,minute,se))
#p.85 응용 예제 3번 근무시간
work = int(input('4자리 사원번호를 입력하세요. >>>'))

time = work % 10

result = '오전' if time >= 5 else '오후'
print('근무 시간은 %s입니다.'%result)
#p.86 응용 예제 4번 라면
print('한 박스에 20개의 라면을 담을 수 있습니다.')
print('라면의 개수를 입력하시면 필요한 박스 수를 알려드립니다.')
ram = int(input('라면의 개수를 입력하세요 >>> '))
ra = ram//20
rae = ram % 20
res = ra+1 if rae>0 else ra
print('%d개 라면을 담으려면 %d박스가 필요합니다.'%(ram,res))
#p.86 응용 예제 5번 평균
k = int(input('국어 점수를 입력하세요. >>> '))
e = int(input('영어 점수를 입력하세요. >>> '))
m = int(input('수학 점수를 입력하세요. >>> '))

t = k + e+ m
avg = t/float(3)

re = '합격' if avg>=80 else '불합격'

print('평균은 %.1f이고, 결과는 %s입니다.'%(avg, re))
