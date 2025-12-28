def solution(participant, completion):
    answer = ""
    people_dict = {}  # 해시 알고리즘 적용 
    for p in participant: 
        if p in people_dict: # 주의 
            people_dict[p] += 1 
        else: 
            people_dict[p] = 1 
    
    for c in completion: # 주의
        if people_dict[c] == 1: # 주의 
            del people_dict[c] 
        else: 
            people_dict[c] -= 1 
    
    answer = list(people_dict.keys())[0] #리스트로 한 것의 [0]
    return answer  # def에서 출력값은 return인거 기억하자. 

a = ["mislav", "stanko", "mislav", "ana"]
b = ["stanko", "ana", "mislav"]
solution(a, b)
print(solution(a,b))