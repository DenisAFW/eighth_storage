# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.
import pickle
import csv


# my_dict = {'1': 'Alexa',
#            '2': 'Rick',
#            '3': 'Morty'}

# with open('test.pickle', 'wb') as pic_f:
#     pickle.dump(my_dict, pic_f)
def to_csv(file_name):
    with (open(file_name, 'w', newline='') as csv_f, open('test.pickle', 'rb') as pic_r):
        pic_read = pickle.load(pic_r)
        pic_read = [pic_read]
        keys = pic_read[0].keys()
        dict_writer = csv.DictWriter(csv_f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(pic_read)


if __name__ == '__main__':
    to_csv('test.csv')
