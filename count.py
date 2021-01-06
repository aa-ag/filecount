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
    df.index += 1
    print(df)
    '''
        Directory Name             Last Modified
    1           AboutTime  Sat Jul  4 07:17:19 2020
    2            uploader  Sat Oct 10 07:46:35 2020
    3        urlshortener  Wed Oct 21 16:05:28 2020
    4             scraper  Mon Oct 26 08:36:28 2020
    5   pg13_backend_test  Tue Jul 21 19:34:05 2020
    ..                ...                       ...
    77             xmlpar  Fri Dec 11 20:46:21 2020
    78      ignoresnippet  Thu Dec 24 14:59:51 2020
    79                stt  Mon Nov  9 08:55:38 2020
    80     css_animations  Tue Aug 11 14:46:24 2020
    81          delemails  Fri Nov 20 23:05:33 2020
    '''


###--- DRIVER CODE ---###
if __name__ == "__main__":
    count_directories()


# TO DO: pierce into directoris and count actual files
