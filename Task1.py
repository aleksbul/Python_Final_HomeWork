# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование

import sys
from collections import namedtuple
import os
import logging
import sys

FileObject = namedtuple('FileObject', ['name', 'extension', 'is_directory', 'parent_directory'])
logging.basicConfig(filename='info.log', level=logging.INFO)


def file_info(path):
    files_info = []
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isdir(full_path):
            is_directory = True
            name = file
            extension = None
        else:
            is_directory = False
            name, extension = file.rsplit('.', 1)

        parent_directory = os.path.basename(os.path.dirname(full_path))
        file_object = FileObject(name=name, extension=extension, is_directory=is_directory,
                                 parent_directory=parent_directory)
        files_info.append(file_object)
        logging.info(f'Name: {name}\tExtension: {extension}\tIs_directory: {is_directory}\t'
                     f'Parent directory: {parent_directory}')


if __name__ == '__main__':
    path = sys.argv[1]
    if os.path.exists(path):
        file_info(path)
    else:
        print("The directory doesn't exist")

