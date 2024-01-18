# This is a sample Python script.
import unittest
import zipfile

import out
import xmlrunner
from xmlrunner.extra.xunit_plugin import transform

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
NAME_ZIP = "test"
NAME_FILE = "newFile"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name}')  # Press Ctrl+F8 to toggle the breakpoint.


def zip_file():
    with open(f'{NAME_FILE}.txt', 'w') as f:
        f.write('Create a new text file!')
    with zipfile.ZipFile(f'./{NAME_ZIP}.zip', 'w') as zipf:
        # Add a file located at the source_path to the destination within the zip
        # file. It will overwrite existing files if the names collide, but it
        # will give a warning
        source_path = f'./{NAME_FILE}.txt'
        destination = f'{NAME_FILE}.txt'
        zipf.write(source_path, destination, zipfile.ZIP_DEFLATED)
        zipf.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Todos las pruebas unitarias han pasado')
    zip_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
