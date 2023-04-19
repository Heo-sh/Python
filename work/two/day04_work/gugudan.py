#구구단 2단부터 9단까지 출력하는 프로그램

dan = 2

while dan <= 9:
    n = 1
    while n <= 9:
        print('%d * %d = %d' %(dan, n, dan*n))
        n+=1
    dan+=1
