'''
#for in range문으로 1부터 10까지의 합
sum = 0
for i in range(1,11):
    sum = sum + i
print(sum)

#while문으로 1부터 10까지의 합

hap = 0 # hap과 n은 초기값이다.

n= 1

while n <= 10: #while 조건식:
    hap = hap + n # 출력문
    n = n + 1 # 제어식
print(hap)
print('-----------------------------------------------')
hap = 0

n= 1

while n <= 10: #제어식과 출력문을 바꿧을 때 결과 : 65
    n = n + 1
    hap = hap + n 
print(hap)
print('---------------------------------')

hap = 0

n= 1

while n <= 10: #출력문이 while조건식에서 빠졌을 때 결과 : 11
    n = n + 1
hap = hap + n 
print(hap)
'''
print('-------------------------------------------------')

hap = 0 

n= 1

while n <= 10: 
    hap = hap + n 
    n = n + 1
    print(n-1,'->', hap, end=',')

print('----------------------------------------------')

hap = 0 

n= 1

while n <= 10:
    n = n + 1
    hap = hap + n 
    print('%d %s %d'%(n, '->', hap))

















    
