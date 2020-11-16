'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника.
 В расчете необходимо использовать формулу:
 (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо
 запускать скрипт с параметрами.
'''
from sys import argv
# argv = ['task1.py', '10', '5', '7']
print(argv)

# C:\Projects\pythonProject2\venv\Users\Genady\Project\python_basic_30_10_2020\Scripts\
# python.exe task1.py
#C:/Users/Genadiy/Project/python_basic_30_10_2020/task1.py
output = int(argv[1]) # выработка в часах
rate = int(argv[2])  # ставка в час
prize = int(argv[3])  # премия
total = output * rate + prize  # заработная плата
print(total)
