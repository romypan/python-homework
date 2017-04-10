import random
x = random.randint(1,10)
count =0 
strinput = input('Please input 1-10 random int number: ')

if int(strinput) == x:
    print(str(x))
else:
    while int(strinput) != x:   
        strinput = input('not right,value='+str(x)+' please input agagin: ')
        x = random.randint(1,10)
        count = count+1
        if count > 3:
            break
        if int(strinput) == x:
            print('game over '+str(x))

      


    
