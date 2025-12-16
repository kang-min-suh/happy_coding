def find_second_max(array): 
    if array[0] > array[1]: 
        first = array[0]
        second = array[1]
    else: 
        first = array[1]
        second = array[0]

    for num in array[2:]: 
        if num > first:
            second = first
            first = num 
        elif second < num < first: 
            second = num 
  
    return second 
 
print("정답 = 5 / 현재 풀이 값 = ", find_second_max([3, 5, 6, 1, 2, 4]))


