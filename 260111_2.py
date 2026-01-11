data_int = input().split()
data_set = set(data_int)
# data_set
data_dict = {}
for key in data_set: 
    data_dict[key] = data_int.count(key)

max(data_dict, key = data_dict.get)
print(f'{max(data_dict, key = data_dict.get)}(이)가 총 {max(data_dict.values())}표로 반장이 되었습니다.')