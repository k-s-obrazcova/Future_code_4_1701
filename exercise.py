import glob
import os.path

files = glob.glob('./*.py')
for file in files:
    print(file)
    file_size = os.path.getsize(file)
    print(f"Размер файла {file} - {file_size} байт")
