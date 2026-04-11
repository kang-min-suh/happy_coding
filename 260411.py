def math(e): 
    count = 0
    for i in e: 
        if i == '(': 
            count += 1
        elif i == ')': 
            count -= 1
    if count == 0: 
        return True
    else: 
        return False
    
