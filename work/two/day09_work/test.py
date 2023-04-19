number = [ [1,2,3,4,5],
           [6,7,8,9,10],
           [11,12,13,14,15]
         ]

sum = 0;
for i in range(0,3):
    for j in range(0,5):
        sum+=number[i][j]

print(sum)
