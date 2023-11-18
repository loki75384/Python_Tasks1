# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

import random

# sp = [1,2,3,2,3]
print(sp:= [random.randint(1,10) for _ in range(10)])
counter = 0
for i in set(sp): # проходимся по уникальным значениям списка
    counter += sp.count(i) // 2
print(counter)
    
        
        