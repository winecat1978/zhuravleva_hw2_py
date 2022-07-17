# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. Факториал
# 5! = 120

num = int(input("Введите число: "))
i = 1
factorial = 1
while i <= num:
    factorial = factorial * i
    i+=1

print(factorial)
