#for문을 이용하여 구구단 단 1개 출력
dan = int(input('출력할 구구단을 입력하세요. >>>'))

for i in range(1,10):
    print('%d x %d = %d'%(dan, i, dan*i))
