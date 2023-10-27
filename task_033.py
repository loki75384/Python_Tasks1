# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def replace_estimation(array, i, max_num):
    if i == -1:
        return
    if array[i] == max_num:
        array[i] = min(array)
    return replace_estimation(array, i - 1, max_num)

array = [1, 3, 3, 3, 4]
replace_estimation(array, len(array)-1, max(array))
print(*array)


        
        


