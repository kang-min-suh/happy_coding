def prime_list(n): 
    sieve = [True]*n
    m = int(n**0.5)
    for i in range(2, m+1): 
        if sieve[i] == True: 
            for j in range(i*i, n, i): 
                sieve[j] = False
    return[i for i in range(2, n) if sieve[i] == True]

prime_set = set(prime_list(100))
n = int(input())

parti = []
l = [[i, n-i] for i in range(n//2 +1) if i in prime_set and n-i in prime_set]
print(l)