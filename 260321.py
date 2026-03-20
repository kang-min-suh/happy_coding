h,w = map(int, input().split()) # height, width 정보를 입력
# h x w 개수만큼 특정 숫자를 입력 (-21~21억)
# 이 너무 큰 숫자들은 -> list로 [list comprehension]으로 만들수 없다. 
# + 음수가 존재하기에, dictionary 사용 

d = {}
# key : [위치, 위치, 위치..] 

for i in range(h):
  row_info = list(map(int, input().split()))
  # row_info에 들어간 모든 값들을 하나씩 dictionary에 저장
  for j in range(w):
    # row_info[j]번째 값은 (i,j) 위치에 있어요! 라고 기록
    if d.get(row_info[j]) == None: # 이 row_info[j]라는 값이 아직 기록된적이 없다면 
    # if row_info[j] not in d.keys()
      # 새로운 리스