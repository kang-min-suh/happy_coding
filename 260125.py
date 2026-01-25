x = int(input())
if x <= 1:
    print('소수가 아닙니다.')
elif x == 2: 
    print('소수입니다.')   
else: 
    for i in range(2, x): 
        if x % i == 0: 
            print('소수가 아닙니다.')
            break 
    else: 
        print('소수입니다.')