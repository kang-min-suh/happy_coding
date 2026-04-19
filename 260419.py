
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
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
def func1(humidity, val_set):
    if humidity < val_set:
        return 
 3

    return 1

def func2(humidity):
    if humidity >= 50:
        return 0
    elif humidity >= 40:
        return 1
    elif humidity >= 30:
        return 2
    elif humidity >= 20:
        return 3
    elif humidity >= 10:
        return 4
    
else: 

        
return 5


def func3(humidity, val_set):
    if humidity < val_set:
        return 1
    return 
 0


def solution(mode_type, humidity, val_set):
    answer = 0
    if mode_type == "auto":
        answer = func
2(humidity)

    elif mode_type == "target":
        answer = func
1(humidity, val_set)

    elif mode_type == "minimum":
        answer = func
3(humidity, val_set)

    return answer