# Вклад в банке составляет X рублей. 
# Ежегодно он увеличивается на P процентов, после чего дробная часть копеек отбрасывается.
# Требуется определить: через сколько лет вклад составит не менее Y рублей.

X = float(input("Какой величины вклад в банке? Х = "))
P = float(input("Введите % в десятичной форме. P = "))
Y = int(input("Какая сумма должна быть достигнута? Y = "))

year_count = 0

while X < Y:
    year_count +=1
    X = X*(1+P)
    X = X // 1
print(year_count)