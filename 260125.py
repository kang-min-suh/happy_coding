user_input = input()
user_input = list(map(int, user_input.split()))

def sol(l): 
    l = sorted(l)
    for i in range(len(l)-1): 
        if l[i] + 1 != l[i+1]: 
            return "NO"
    return "YES"

print(sol(user_input))