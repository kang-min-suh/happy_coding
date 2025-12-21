#  3을 포함하면 "짝", 그외에는 해당숫자를 출력하는 게임

try: 
    input_num = input("원하는 숫자를 입력해주세요: ")
    num = int(input_num)
    if '3' in input_num: 
        print("짝")
    else: 
        print(num)

except ValueError: 
    print("숫자를 입력해주세요")
