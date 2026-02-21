

def solution(block_all, rule):
    for block_part in block_all:
        if block_check(block_part, rule) == '불가능':
             return '불가능'
    return '가능'
        

def block_check(block_part, rule): 
    dummy_value = rule.index(rule[0])
    for char in block_part: 
        if char in rule: 
                used_chars = True
                if dummy_value > rule.index(char): 
                     return '불가능'
                used_chars = False
                dummy_value = rule.index(char)
    if not used_chars: 
         return '불가능'
    return '가능'


block_all = input().split(' ')
rule = input()

print(solution(block_all, rule))