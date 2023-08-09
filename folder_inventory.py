import os
import time
from datetime import datetime, date


print("""
   __        _      _               _                           _                      
  / _|      | |    | |             (_)                         | |                     
 | |_  ___  | |  __| |  ___  _ __   _  _ __ __   __ ___  _ __  | |_  ___   _ __  _   _ 
 |  _|/ _ \ | | / _` | / _ \| '__| | || '_ \\ \ / // _ \| '_ \ | __|/ _ \ | '__|| | | |
 | | | (_) || || (_| ||  __/| |    | || | | |\ V /|  __/| | | || |_| (_) || |   | |_| |
 |_|  \___/ |_| \__,_| \___||_|    |_||_| |_| \_/  \___||_| |_| \__|\___/ |_|    \__, |
                                                                                  __/ |
                                                                                 |___/ 
""")
print('Скрипт для инвентаризации файлов в корневых папках v1.0. Q4-2021'.upper())
kornevaya = input('\nВведите путь к папке для инспекции, в формате "C:\\Новая папка\\...\\" : ')
print('Тестируемая папка: ', kornevaya)

dt_now = str(datetime.now())
tek_date = str(date.today())
print('Текущая дата: ', tek_date, '\n')
Koren = [i[0] for i in os.walk(kornevaya)]

address = []    # Ссылки на все файлы
pi = 0          # 'Питоновских файлов в папке = '
tx = 0          # 'Текстовых файлов в папке = '
xl = 0          # 'Эксель файлов в папке = '
doc = 0
neizvest = 0
for add, pap, fil in os.walk(kornevaya):
    for files in fil:
        full = os.path.join(add, files)
        address.append(full)
# print('\nФайл: ', address[2], '\n Дата последнего изменения: ', time.ctime(os.path.getmtime(address[2])))
for i in address:
    if '.py' in i:
        pi += 1
        print(os.path.basename(i), '(Дата последнего изменения: ----------', time.ctime(os.path.getmtime(i)), ')')
    if '.txt' in i:
        tx += 1
        print(os.path.basename(i), '(Дата последнего изменения: ----------', time.ctime(os.path.getmtime(i)), ')')
    if '.xls' in i:
        xl += 1
        print(os.path.basename(i), '(Дата последнего изменения: ----------', time.ctime(os.path.getmtime(i)), ')')
    if '.doc' in i:
        doc += 1
        print(os.path.basename(i), '(Дата последнего изменения: ----------', time.ctime(os.path.getmtime(i)), ')')
    if '.py' not in i and '.txt' not in i and '.xls' not in i and '.doc' not in i:
        neizvest += 1
        print(os.path.basename(i), '(Дата последнего изменения: ----------', time.ctime(os.path.getmtime(i)), ')')


print('\nВсего в файлов в корневом каталоге - ', pi + tx + xl + doc + neizvest, '\n'*2, Koren[0], '\n'*2, 'Их них файлы с расширениями:')
print('     Питоновских файлов в папке = ', pi)
print('     Текстовых файлов в папке = ', tx)
print('     Экселевских файлов в папке = ', xl)
print('     Вордовских файлов в папке = ', doc)
print('     !!!!! НЕИЗВЕСТНЫЙ ФОРМАТ !!!!!  в папке = ', neizvest)

# Вывод данных в txt. Создам текст
allfiles = pi + tx + xl + doc + neizvest
enter2, enter5 = ('\n'*2), ('\n'*5)

file_name = f'\Инвентаризация {tek_date}.txt'
paths="\\".join(str(os.path.dirname(os.path.realpath(__file__))).split(os.sep)) + file_name
with open(paths, 'w') as ouf:
    ouf.write(str('••••••••••••••••••••••••••••••••••' + '\n' + '••Дата выгрузки лога: ' + str(tek_date)) + '••\n' + '••••••••••••••••••••••••••••••••••')
    ouf.write(str(enter5 + ('Всего файлов в корневом каталоге - ' + str(allfiles) + enter2 + str(Koren[0]) + enter2 +
                  'Их них файлы с расширениями:' + enter2 + '     Питоновских файлов в папке = ' + str(pi) + '\n' +
                  '     Текстовых файлов в папке = ' + str(tx) + '\n' + '     Экселевских файлов в папке = ' + str(xl) +
                  '\n' + '     Вордовских файлов в папке = ' + str(doc) + '\n' + '     !!!!! НЕИЗВЕСТНЫЙ ФОРМАТ !!!!!  в папке = ' + str(neizvest))))
    ouf.write(str(enter5 + 'LIST OF FILES: \n'))
    ouf.write('\n' + 'PYTHON3: ' + '\n')
    for i in sorted(address):
        if '.py' in i:
            ouf.write(str('\t' + (os.path.basename(i))) + '\t(Дата последнего изменения: ----------' + str(time.ctime(os.path.getmtime(i))) + ')' + '\n')
    ouf.write('\n' + 'ТЕКСТОВЫЙ РЕДАКТОР - БЛОКНОТ: ' + '\n')
    for i in sorted(address):
        if '.txt' in i:
            ouf.write(str('\t' + (os.path.basename(i))) + '\t(Дата последнего изменения: ----------' + str(time.ctime(os.path.getmtime(i))) + ')' + '\n')
    ouf.write('\n' + 'EXCEL: ' + '\n')
    for i in sorted(address):
        if '.xls' in i:
            ouf.write(str('\t' + (os.path.basename(i))) + '\t(Дата последнего изменения: ----------' + str(time.ctime(os.path.getmtime(i))) + ')' + '\n')
    ouf.write('\n' + 'WORD: ' + '\n')
    for i in sorted(address):
        if '.doc' in i:
            ouf.write(str('\t' + (os.path.basename(i))) + '\t(Дата последнего изменения: ----------' + str(time.ctime(os.path.getmtime(i))) + ')' + '\n')
    ouf.write('\n' + '!!!!! НЕИЗВЕСТНЫЙ ФОРМАТ !!!!! : ' + '\n' if neizvest > 0 else "\n\n\nСПАСИБО ЗА ВНИМАНИЕ")
    for i in sorted(address):
        if '.py' not in i and '.txt' not in i and '.xls' not in i and '.doc' not in i:
            ouf.write(str('\t' + (os.path.basename(i))) + '\t(Дата последнего изменения: ----------' + str(time.ctime(os.path.getmtime(i))) + ')' + '\n')

end = input('\n\nСПАСИБО ЗА ВНИМАНИЕ')
# with open('C:\\Users\OperatorDZ\Desktop\pyprod\Задача 3.txt', encoding="utf-8") as inf:
#     text = inf.read().strip()
#     textspis = [i for i in text.strip().split(';')]
#      return os.stat(filename).st_mtime  
# print(textspis)    