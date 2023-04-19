#while_continue문
#사용자로부터 원하는 양수를 입력 받아 0부터 홀수 값을 출력하라.
'''
n = int(input('원하는 양수'))

i = 0

while i < n: #조건식
    i = i + 1 #변환식
    if i % 2 == 0: #단순 if문
        continue
    print(i)

#for in range문

n = int(input('원하는 양수 : '))

for i in range(0,n+1):
    if i % 2 == 0:
        continue
    print(i)
'''
'''
n = int(input('원하는 양수'))

i = 0

while i < n:
    print(i)
    i += 1
    if i % 2 == 0:
        continue
    
위의 식 경우 print(i)가 먼저 출력이 되며,
while 조건문에 의해서 i는 입력받은 n의 값보다
작을 때까지 반복하는 조건에서만 출력을 하게 된다.
이때, if문은 소용이 없게 된다.
'''
#이번에는 입력받은 값에서 짝수만 나오게 하라
'''
n = int(input('정수를 입력하라 >>> '))

i = 0

while i < n:
    i += 1
    if i % 2 != 0:
        continue
    print(i)
'''
#3의 배수를 출력하라
'''
n = int(input('정수 입력 >>> '))

i = 0

while i < n:
    i += 1
    if i % 3 != 0:
        continue
    print(i)
'''

#3의 배수를 for문으로 하라

n = int(input('정수 입력 >>> '))

for i in range(0,n+1):
    if i % 3 != 0:
        continue
    print(i)
























