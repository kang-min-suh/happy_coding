# 강사님 풀이 (2번째 버전)
%%timeit
def check_prime(n): 
    if n <= 1: 
        return "NO"
    i = 2 
    prime = True
    while (i**2) < n : 
        if n % i == 0: 
            prime = False
            break
        i += 1 
    if prime: 
        return "YES"
    else: 
        return "NO"