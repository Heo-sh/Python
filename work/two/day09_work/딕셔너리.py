student = {'name':'홍길동','e-mail':'hong@gmail.com','tel':'010-1111-1111'}

print(student)

#데이터의 수정 -> 존재하는 키값
student['name'] = '이현준'
print(student)

#데이터의 추가 -> 존재하지 않는 키값
student['address'] = '서울시'
print(student)

#데이터의 삭제
del(student['e-mail'])
print(student)


#keys() : 모든 키값들 만 출력
print(student.keys())

#values()
print(student.values())

#items()
print(student.items())

# in : key의 존재 여부를 확인할  때 사용합니다.
print(student)
print('name' in student)
print('홍길동' in student)





























