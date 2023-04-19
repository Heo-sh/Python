'''
#for문에서도 break를 사용할 수 있다.
for i in range(0,100):
    print(i)
    if i == 9:
        break
'''
i = 0
while True:
    print(i) #실행문
    i+=1 #조건식
    if i == 9: #단순 if문
        break

for i in range(0,100):
    if i == 10:
        break
    print(i)

#while문의 무한루프로 1부터 10까지의 합을 구하라

sum = 0
i = 1
while True:
    sum = sum + i
    i = i + 1
    if i > 10: #if 조건식이 참인 경우 break
        break
print(sum)

#for문과 break문으로 1부터 10까지의 합을 구하라.

hap = 0
for i in range(1,100):
    hap = hap + i
    if i >= 10:
        break
print(hap)
