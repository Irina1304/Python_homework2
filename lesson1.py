#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#0,56 -> 11

input_number = input('Введите число: ')
sum = 0
for i in input_number:
    if i.isdigit():
        sum += int(i)

print(sum)

