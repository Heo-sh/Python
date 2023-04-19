#2단부터 ~9단까지 이중 for문을 통해 출력을 해보자
'''
for i in range(2,10):
    for j in range(1,10):
        print('%d x %d = %d'%(i,j,i*j))
    print()
'''

''' * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
'''
'''
for i in range(5):
    for j in range(5):
        print('*',end='')
    print()
'''
'''
    *
    * *
    * * *
    * * * *
    * * * * *
'''

for i in range(5):
    for j in range(5):
        if j<= i:
            print('*',end='')
    print()

'''
    * * * * *
      * * * *
        * * *
          * *
            *
'''










    
