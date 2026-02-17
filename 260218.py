value = int(input())

result = 0 

while True: 
    if value %7 == 0: 
        result += value // 7
        print(result)
        break
    value -= 3 
    result += 1 
    if value < 0: 
        print(-1)
        break