# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import sys
import os
import pickle

sys.path.insert(0, '../seventh_storage')

from task_4 import make_files


def main():
    create_file()
    print(find_file())


def create_file():
    make_files('json', count=1)


def find_file():
    file_list = os.listdir()
    for ext in file_list:
        if '.json' in ext:
            with (open(ext, 'rb') as json_file, open('my_dict.pickle', 'wb') as f):
                text = json_file.read()
                pickle.dump(ext, f)
                pickle.dump(text, f)
    return 'Good'


if __name__ == '__main__':
    main()
