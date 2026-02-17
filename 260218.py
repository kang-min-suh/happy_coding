input_weight = int(input())  # 정량을 입력

cnt = 0
def eli_count(input_weight): 
    if (input_weight % 7) or (input_weight % 3) == 0: 
        cnt += (input_weight //7) + (input_weight //3)
        print(cnt)
    else: 
        print(-1)