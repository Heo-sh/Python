#로또번호 자동 생성
import random  #random모듈 안에 있는 randint를 사용하겠다.


a = 0

lotto = []

for i in range(6):
    a = random.randint(1,45) 
    lotto.append(a)

print(lotto)
