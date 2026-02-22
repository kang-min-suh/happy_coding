# block_all, block_part, rule, char, dummy_value, flag_value


def solution(block_all, rule):
    for block_part in block_all:
        if rule_check(block_part, rule) == '불가능':
            return '불가능'
    return '가능'

def rule_check(block_part, rule): 
    dummy_value = rule.index(rule[0])
    flag_value = False 
    for char in block_part:
        if char in rule: 
            flag_value = True 
            if dummy_value > rule.index(char): 
                return '불가능'
    if not flag_value: 
        return '불가능' 
    return '가능'
        

block_all = input().split(' ')
rule = input()

print(solution(block_all, rule))