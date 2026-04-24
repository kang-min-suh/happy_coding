s = input("입력:") # 입력: HumanDev

x = []
for i in s.split(): 
    x.append(i[::-1])
y = ' '.join(x)
z = ''.join([c for c in y if c not in 'ong'])
print(z)