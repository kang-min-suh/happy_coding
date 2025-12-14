student_names = ["영희", "현준", "딩코", "코딩"]
student_heights = [166, 198, 188, 100]

def get_180_over_indexes(heights): 
    result = []
    for i in range(len(heights)): 
        height = heights[i]
        if height > 180: 
            result.append(i)
    return result 

over_indexes = get_180_over_indexes(student_heights)

for i in over_indexes: 
    print(student_names[i])