import os
import sys


def find_duplicates(dir_path):
    files_dict = {}
    for path, dirs, files in os.walk(dir_path):
        for file in files:
            full_path = os.path.join(path, file)
            filesize = os.path.getsize(full_path)
            if not (file, filesize) in files_dict:
                files_dict[(file, filesize)] = [full_path]
            else:
                files_dict[(file, filesize)].append(full_path)
    dupes_filter = dict((file, paths) for file, paths in files_dict.items() if len(paths) > 1)
    return dupes_filter

def list_file_dublicates(dir_path):
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        dublicates = find_duplicates(dir_path)
        for file, paths in dublicates.items():
            print("Файл {filename} имеет следующие дубликаты:".format(filename=file[0]))
            for path in paths:
                print(os.path.abspath(path))
    else:
        print("Указан неверный путь к директории")

if __name__ == '__main__':
    try:
        list_file_dublicates(sys.argv[1])
    except IndexError:
        print('Не указан путь к файлу')
