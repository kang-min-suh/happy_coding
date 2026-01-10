def one(n): 
    def two(m): 
        return m**n
    return two

a = one(3)
print(a(3)) 