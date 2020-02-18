Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
print()
print('Задача 1')
print()

i  = 0
for i in range(1, 6):
    print(i, 0)
    i += 1

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print()
print('Задача 2')
print()

i = 0
count = 0
for i in range(1, 11):
    print('№', i)
    num = 100
    while num/10 > 1:
        num = int(input('Введите одну цифру: '))
    if num == 5:
        count += 1
print('Цифру 5 Вы ввели', count, 'раз.')
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
print()
print('Задача 3')
print()
sum = 0

for i in range(1, 101):
     sum += i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
print()
print('Задача 4')
print()

prod = 1
for i in range(1, 11):
    prod *= i
print(prod)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
print()
print('Задача 5')
print()

# integer_number = 2129
#
# while integer_number > 0:
#     a = []
#     integer_number % 10 = list.append(a)
#     integer_number = integer_number//10

# выводит, начиная с первой цифры
integer_number = 2129
a = []

while integer_number > 0:
    a.append(integer_number % 10)
    integer_number = integer_number//10
a.reverse()
for i in range(len(a)):
    print(a[i])


'''
Задача 6
Найти сумму цифр числа.
'''
print()
print('Задача 6')
print()

num = int(input('Введите число: '))
sum = 0

while num > 0:
    sum += num % 10
    num = num//10
print(sum)

'''
Задача 7
Найти произведение цифр числа.
'''
print()
print('Задача 7')
print()

num = int(input('Введите число: '))
prod = 1

while num > 0:
    prod *= num%10
    num = num//10
print(prod)



'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
print()
print('Задача 8')
print()

integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
print()
print('Задача 9')
print()
max = 0
num = int(input('Введите число: '))
while num > 0:
    if num%10 >= max:
        max = num % 10
    num = num//10
print(max)


'''
Задача 10
Найти количество цифр 5 в числе
'''

print()
print('Задача 10')
print()

num = int(input('Введите число: '))
sum_of_5 = 0
while num > 0:
    if num%10 == 5:
        sum_of_5 +=1
    num = num//10
print('Количество цифр 5 в числе:', sum_of_5)
