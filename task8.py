# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

y = int(input('год: '))

if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
    print("Год високосный")
else:
    print("Год невисокосный")
