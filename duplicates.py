import os
import sys


def find_duplicates(dir_path):
    # list of dicts for files (name, size, path)
    files_dict = []
    # set of pairs 'file - filesize'
    files_set = set()
    for path, dirs, files in os.walk(dir_path):
        for file in files:
            full_path = os.path.join(path, file)
            filesize = os.path.getsize(full_path)
            file_dict = {}
            file_dict["name"] = file
            file_dict['size'] = filesize
            file_dict['path'] = full_path
            files_dict.append(file_dict)
            files_set.add((file, filesize))

    # dict with full paths to file for pair 'name - filesize'
    dupes = {}
    for name, size in files_set:
        for item in files_dict:
            if item['name'] == name and item['size'] == size:
                if dupes.get((name, size)):
                    dupes[(name, size)].append(item['path'])
                else:
                    dupes[(name, size)] = [item['path']]

    dupes_filter = dict((file, paths) for file, paths in dupes.items() if len(paths) > 1)
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
        print(list_file_dublicates(sys.argv[1]))
    except IndexError:
        print('Не указан путь к файлу')

