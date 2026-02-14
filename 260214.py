import re 
input_srt = input()

range_base = re.findall('(\\w)(\\1*)', input_srt)

s = ''
for i, j in range_base: 
    s += i + str(len(j) + 1)
print(s)