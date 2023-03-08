import os.path
from zipfile import ZipFile

def in_excluded_folder(file, excludes):
    excluded_folders = [x for x in excludes if x[-1] == '/']
    file = file.replace('\\', '/')
    for folder in excluded_folders:
        if file[:len(folder)] == folder:
            return True
    return False

def zip(zip_filename, folder, excludes = []):
    with ZipFile(zip_filename, 'w') as zip:
        # Iterate over all the files in directory
        for folder_name, subfolders, filenames in os.walk(folder):
            for filename in filenames:
                # create complete filepath of file in directory
                file_path = os.path.join(folder_name, filename)
                file = os.path.basename(file_path)
                if file in excludes or file[0] == '.':
                    continue

                relative = os.path.relpath(file_path, folder)
                if relative[0] == '.' or in_excluded_folder(relative, excludes):
                    continue
                # Add file to zip
                print(f'{relative}')
                zip.write(file_path, relative)

try:
    os.remove('seasons.zip')
except OSError:
    pass
zip('seasons.zip', '.', ['templates/', 'vanilla/', 'build.py', 'CONTRIBUTING.md', 'Notes.txt', 'package.py', 'seasons.zip', 'credentials.json', 'metadata.json'])
