'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
 При этом английские числительные должны заменяться на русские.
 Новый блок строк должен записываться в новый текстовый файл.
'''

with open('f_4.txt', 'r', encoding='utf-8') as f:
    count_lines = f.readlines()
    my_list = []
    my_list_rus = ['один', 'два', 'три', 'четыре']

    for i in range(len(count_lines)):
        my_list.append(my_list_rus[i] + ' ' + ' '.join(count_lines[i].split()[1:]) + '\n' )

with open('f_4_1.txt', 'w', encoding='utf-8') as f_1:

   f_1.writelines(my_list)


