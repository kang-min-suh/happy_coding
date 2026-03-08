user_input = input()
s = ''
storeString = user_input()
count = 0
for i in user_input:
    if i == storeString: 
        count += 1
    else: 
        s += storeString + str(count)
        storeString = i 
        count = 0
s += storeString + str(count)
print(s)