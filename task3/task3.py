# Задана последовательность натуральных чисел, завершающаяся числом 0. 
# Требуется определить значение второго по величине элемента в этой последовательности, 
# то есть элемента, который будет наибольшим, если из последовательности удалить наибольший элемент.

from operator import index


numbers = [6, 9, 8, 2, 0] # можно задать вручную
l = len(numbers)
max1 = numbers[0]
for i in range(l):
    if numbers[i] > max1:
        max1 = numbers[i]
        i+=1
index = numbers.index(max1)
numbers.pop(index)
l2 = len(numbers)
max2 = numbers[0]
for i in range(l2):
    if numbers[i] > max2:
        max2 = numbers[i]
        i+=1
print(max2)

