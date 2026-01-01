try: 
    height = int(input("키를 입력해주세요: "))
    if height > 150: # 문제에서는 150을 넘으면 이라고 했으니까 초과의 의미로
        print("Yes")
    else: 
        print("No")
except ValueError: 
    print("숫자로 입력해주세요")

## 주의할 점(한번 수정함!): try 구문에서부터 height가 들어가야함!!! 