# 변수를 정하자 

# block_all
# block_part 
# rule 
# dummy_value 
# flag_value 

# def1의 구조: solution 


def solution(block_all, rule): 
    for block_part in block_all: 
        if rule_check(block_part, rule) == '불가능': 
            return '불가능'
    return '가능'

# def2의 구조: rule_check 
def rule_check(block_part, rule): 
    dummy_value = rule.index(rule[0])
    flag_value = False
    for char in rule: ############
        if char in rule: 
            flag_value = True 
            if dummy_value > rule.index(char): 
                return '불가능'
            dummy_value = rule.index(char)
    if not flag_value: 
        return '불가능'
    return '가능'

block_all = input().split(' ')
rule = input()
print(solution(block_all, rule))