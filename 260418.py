
2
3
4
5
6
7
8
9
10
11
12
13
def solution(route):
    east = 0
    north = 0
    for i in route:
        if i == "N":
            north += 1
        elif i == "S" :
            
north -= 1

        elif i == "E" :
            
east += 1

        elif i == 
"W"
 :
            
east -= 1

    return [east, north]