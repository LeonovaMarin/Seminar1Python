# Задача 6
# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#  Пример:
# 385916 -> yes
# 123456 -> no

n = int(input('введите шестизначный номер билета'))
print(n)
n1 = n // 100000
n2 = (n % 100000)//10000
n3 = (n % 10000)//1000
n4 = (n % 1000)//100
n5 = (n % 100)//10
n6 = n % 10
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)

res1 = n1 + n2 + n3
res2 = n4 + n5 + n6
if res1 == res2:
    print('билет счастливый')
else:
    print('билет несчастливый')
