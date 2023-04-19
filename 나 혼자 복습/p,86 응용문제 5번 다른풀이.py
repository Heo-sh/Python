'''
k = int(input('국어 점수를 입력하세요>>> '))
e = int(input('영어 점수를 입력하세요>>> '))
m = int(input('수학 점수를 입력하세요>>> '))

total = k+e+m

ave = total/float(3)

if ave >= 80:
    print('평균은 %.1f점이고, 결과는 합격입니다.'%ave)
else:
    print('평균은 %.1f점이고, 결과는 불합격입니다.'%ave)
'''
print('-------------------------------------------------')

k = int(input('국어 점수를 입력하세요>>> '))
e = int(input('영어 점수를 입력하세요>>> '))
m = int(input('수학 점수를 입력하세요>>> '))

total = k+e+m

ave = total/float(3)

i = '합격' if ave >= 80 else '불합격'

print('평균은 %.1f점이고, 결과는 %s입니다.'%(ave, i))
