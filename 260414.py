
2
3
4
5
6
7
8
def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in 
cpr
:
        for i in 
range(len(basic_order))
:
            if action == basic_order[i]:
                answer.append(
i+1
)
    return answer