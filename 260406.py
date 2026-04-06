from itertools import permutations, combinations
user_input = input().split(',')
user_input_int = int(input())

print(list(map(''.join, combinations(user_input, user_input_int))))
print(len(list(combinations(user_input, user_input_int))))