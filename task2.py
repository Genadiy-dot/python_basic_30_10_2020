'''
Создать текстовый файл (не программно),
 сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''
import sys

#my_f = sys.argv[1]# список аргументов командной строки
my_f = "f_2.txt"

#lines = 0  # подсчёт строк,слов,символов
#content = 0

with open('f_2.txt', 'r') as f:  # применение менеджера контекста
     f.read().split()   # чтение файла,разделение файла на слова
     f.readlines()
    #pos = 'out' # нахождение за пределами слова

    print('f.read().split(): ', f.read().split())


print('f.readlines(): ', f.readlines())