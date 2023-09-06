pattern_list = [1, 2, 3, 4, 5, 6]
print(pattern_list)

num = 2

first_list = pattern_list[num:num]
print(first_list)

second_list = pattern_list[:num]
print(second_list)

third_list = pattern_list[num:]
print(third_list)

fourth_list = pattern_list[:-num]
print(fourth_list)

fifth_list = pattern_list[-num:]
print(fifth_list)