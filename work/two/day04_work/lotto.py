#로또번호 자동 생성기
import random


a = 0

lotto = []

for i in range(6):
    a = random.randint(1,45)
    lotto.append(a)

print(lotto)
