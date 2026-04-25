def f(a): 
    m = [[x] for x in a]
    b = m[:]
    for i in range(len(b)-1): 
        b[1+i] += b[i]
    result = sum([[len(x) for x in m]])
    return result 
print(f([1, 2, 3, 4]))