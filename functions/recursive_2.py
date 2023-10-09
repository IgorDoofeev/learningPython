F = {
    'C:': {
        'Python39': ['python.exe, python.ini'],
        'Program Files': {
            'Java': ['README.txt', 'Welcome.html', 'java.exe'],
            'MATLAB': ['matlab.bat', 'matlab.exe', 'mcc.bat']
        },
        'Windows': {
            'System32': ['acedit.dll', 'aclui.dll', 'zipfldr.dll']
        }
    }
}


# Обход словаря
def get_files(path, depth=0):
    for f in path:
        print(' '*depth, f)  # Принт выводит отдельные ключи
        if type(path[f]) == dict:
            get_files(path[f], depth+1)
        else:
            print((' '*(depth+1)), ' '.join(path[f]))  # Вывод списка по определенному каталогу


get_files(F)

