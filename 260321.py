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
      # 새로운 리스트를 투입
      d[row_info[j]] = []
    d[row_info[j]].append((i, j)) # row_info[j]에 적힌 값은 (i,j) 위치에서 발생한다! 
    # 왼쪽위부터 순서대로 보고 있으니, 알아서 정렬은 되어있을것. 

n = int(input())
numbers_to_find = list(map(int, input().split())) # 찾아야 하는 숫자들 

for num in numbers_to_find:
  # 만약 num이라는 숫자가 한번도 발생하지 않았다면 -> "none"이란것을 출력
  if d.get(num) == None:
    print("none")
  else:
    # 이 num이 발생한 모든 위치를 출력
    for pos in d[num]:
      print(f"({pos[0]},{pos[1]})", end=" ")
    print() 