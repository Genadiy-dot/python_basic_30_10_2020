'''
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''
while True:

    num = input('Введите целое число: ')

    if num.isdigit():  # число введено корректно
        num = int(num)
        break
    else:
        print('Ошибка ввода')

result = 0
while num != 0:

    last_digit = num % 10
    num = num // 10

    if last_digit > result:
        result = last_digit
        if result == 9:
            break

print(result)
