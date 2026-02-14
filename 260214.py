import re

input_str = input()

range_base = re.findall('(\\w)(\\1*)', input_str)

s = ''
for i, j in range_base: 
    s += i + str(len(j)+1)
print(s)
