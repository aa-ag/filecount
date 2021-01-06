###--- IMPORTS ---###
import os  # https://docs.python.org/3/library/os.html#os.listdir
# [!] alternatively: glob https://docs.python.org/3/library/glob.html
import settings
import time
import pandas as pd


###--- FUNCTIONS ---###
def count_directories():
    # Use of scandir() to display all the files (excluding directories)
    # in the given path that don’t start with '.';
    # the entry.is_file() call will generally not make an additional system call
    path_to_dirs = settings.DIR_PATH

    directories_names_list = os.listdir(path_to_dirs)
    # print(len(directories_list)) # 81

    directories = list()

    for directory in directories_names_list:
        directories.append([directory, time.ctime(
            os.path.getmtime(path_to_dirs + '/' + directory))])

    df = pd.DataFrame(directories, columns=['Directory Name', 'Last Modified'])
    print(df)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    count_directories()


# TO DO: pierce into directoris and count actual files
