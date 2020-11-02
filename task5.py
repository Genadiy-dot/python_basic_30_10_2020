'''
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
 или убыток — издержки больше выручки). Выведите соответствующее сообщение.
 Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке)
 . Далее запросите численность сотрудников фирмы
и определите прибыль фирмы в расчете на одного сотрудника.
'''

while True:

    proceeds = input('Введите выручку фирмы: ')
    cost = input('Введите издержки фирмы: ')
    worker_count = input('Введите число сотрудников: ')

    if proceeds.isdigit() and cost.isdigit():# корректный ввод числа
        proceeds = int(proceeds)
        cost = int(cost)
        worker_count = int(worker_count)
        break
    else:
        print('Ошибка ввода')


fin_result = proceeds - cost # прибыль или убыток
if fin_result > 0:
    ratio = fin_result / cost #  рентабельность
    print(f'Ваша прибыль равна: {fin_result}, рентабельность: {ratio}')

    profit_of_worker = fin_result / worker_count
    print(f'Прибыль на одного сотрудника составляет: {profit_of_worker}')

elif not fin_result:
    print('Баланс нулевой')
else:
    print('Баланс отрицательный')
