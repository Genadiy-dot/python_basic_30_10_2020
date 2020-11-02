'''
Спортсмен занимается ежедневными пробежками.
 В первый день его результат составил a километров.
 Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
 Требуется определить номер дня,
 на который общий результат спортсмена составить не менее b километров.
  Программа должна принимать значения параметров a и b и выводить
одно натуральное число — номер дня.
'''
while True:

    user_a = input('Введите переменную а: ')
    user_b = input('Введите перемееную b: ')
    day = 1

    if user_a.isdigit() and user_b.isdigit() and user_a[0] != '0' and  user_b[0] != '0':
        user_a = int(user_a)
        user_b = int(user_b)

    while user_a <= user_b:
        user_a *= 1.1 # увеличение числа а на 10 процентов
        day +=1

    print(day)
