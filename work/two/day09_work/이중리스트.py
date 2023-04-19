animals=[
    ['dog','cat','tiger','bear','wolf'],
    ['egle','pelican'],
    ['tuna','shark','salmon']
]
print(animals)
print(animals[0], type(animals[0]))
print(animals[0][2], type(animals[0][2]))
print(animals[0][4])
print(animals[0][-1])

'''
   number = [ [1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15]
            ]
'''
#이중리스트에 있는 각요소들의 합을 출력하는 프로그램을 작성해보세요
# 총 합: x

number = [ [1,2,3,4,5],
           [6,7,8,9,10],
           [11,12,13,14,15]]

total = 0;
for i in range(0,3):
    for j in range(0):
        total += number[i][j]

print(total)
    























