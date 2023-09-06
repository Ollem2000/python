pattern_list = [1, 2, 3, 4, 5, 6]
print(pattern_list)

num = 2

first_list = pattern_list
second_list = pattern_list
third_list = pattern_list
fourth_list = pattern_list
fifth_list = pattern_list

del first_list[num:num]
print(first_list)

del second_list[:num]
print(second_list)

del third_list[num:]
print(third_list)

del fourth_list[:-num]
print(fourth_list)

del fifth_list[-num:]
print(fifth_list)