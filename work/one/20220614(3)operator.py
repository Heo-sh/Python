#사칙연산자
a = 10 
b = 3 

print('%d + %d = %d' %(a,b,a+b)) #+연산자
print('%d - %d = %d' %(a,b,a-b)) #-연산자
print('%d * %d = %d' %(a,b,a*b)) #*연산자
print('%d / %d = %f' %(a,b,a/b)) #/연산자
print('%d //%d = %d' %(a,b, a//b))#//연산자 - 몫만 나온다 float으로 해야 소수점이 나온다.
print('%d **%d = %d' %(a,b, a**b))#**연산자 - 제곱
print('%d %% %d = %d' %(a,a, a%b))#%%연산자 - 나머지가 나온다.(짝수, 홀수 판별할 때 자주 사용)


number1 = 20

number2 = 30

#number1과 number2에 값을 교환하여 저장해보세요. p75
print('number1 = %d, number2 = %d'%(number1,number2))
number1, number2 = number2, number1
print('number1 = %d, number2 = %d'%(number1,number2))

piggy_bank = 0
money = 10000
piggy_bank += money #piggy_bank = piggy_bank + money

print('저금통에 용돈 %d원을 넣었습니다.' %money)
print('지금 저금통에는 %d원이 있습니다.' %piggy_bank)

snack = 2000
piggy_bank -= snack #piggy_bank = piggy_bank - snack

print('저금통에서 과자 구입비 %d원을 뺏습니다.' %snack)
print('지금 저금통에는 %d원이 있습니다.' %piggy_bank)
print('--------------------------------------------------')

a = 15
print('%d > 10 : %s' %(a, a>10))
print('%d < 10 : %s' %(a, a<10))

#파이썬 예약어 33개의 예약어 중 True, False, None
#이 세가지 단어는 대문자를 사용해준다.

print('%d >= 10 : %s' %(a, a>=10))
print('%d <= 10 : %s' %(a, a<=10))
print('%d == 10 : %s' %(a, a==10))
print('%d != 10 : %s' %(a, a!=10))

print('--------------------------------------------------')

a=10
b=0

print('%d > 0 and %d > 0 : %s'%(a,b,a>0 and b<0))
print('%d > 0 or %d > 0 : %s'%(a,b,a>0 or b>0))
print('not %d : %s' %(a, not a))
print('not %d : %s' %(b, not b))
print('--------------------------------------------------')

a = 10
b = 20

result = (a - b) if (a >= b) else (b - a)
print('%d와 %d의 차이는 %d입니다.'%(a,b,result))

K = int(input('국어 점수를 입력하세요 >>>'))
E = int(input('영어 점수를 입력하세요 >>>'))
M = int(input('수학 점수를 입력하세요 >>>'))

total = K + E + M
avg = total/float(3)

result = '합격' if avg>=80 else '불합격'
print('평균은 %.1f점이고, 결과는 %s입니다.'%(avg,result))

































