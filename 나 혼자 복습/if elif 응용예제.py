score = int(input('점수를 입력하세요. >>>'))
if score >= 90:
    print('점수는 %d점이고, 학점은 A학점입니다.'%(score))
elif score >= 80:
    print('점수는 %d점이고, 학점은 B학점입니다.'%(score))
elif score >= 70:
    print('점수는 %d점이고, 학점은 C학점입니다.'%(score))
elif score >= 60:
    print('점수는 %d점이고, 학점은 D학점입니다.'%(score))
else:
    print('점수는 %d점이고, 학점은 F학점입니다.'%(score))

