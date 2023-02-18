import os.path
from zipfile import ZipFile

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
                if relative[0] == '.':
                    continue
                # Add file to zip
                print(f'{relative}')
                zip.write(file_path, relative)

try:
    os.remove('seasons.zip')
except OSError:
    pass
zip('seasons.zip', '.', ['templates', 'vanilla', 'build.py', 'CONTRIBUTING.md', 'Notes.txt', 'package.py', 'seasons.zip'])
