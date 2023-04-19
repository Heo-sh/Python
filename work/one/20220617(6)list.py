li = [10,20,3.1,'heaven'] #서로 다른 자료형 저장 가능
#li = list(100,3.14,'hello')로도 사용가능
print(li)
print(li[0]) # list의 인덱싱

l = [10,20,30,40,50] # list의 슬라이싱
print(l[0:3])

scores = [50,40,30]

scores.append(100) #append 활용 시 100은 맨 뒤에 추가된다.
scores.insert(0,90) #insert 활용 시 저장되는 곳을 지정 가
scores.pop(1)#pop 활용시 지정을 안해주면 뒷 자리가 제거되며, 지정하면 지정된 곳이 제거된다.
print(scores)

t2 =1,2,3
print(t2)
