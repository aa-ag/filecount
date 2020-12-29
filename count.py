###--- IMPORTS ---###
import os  # https://docs.python.org/3/library/os.html#os.listdir
# [!] alternatively: glob https://docs.python.org/3/library/glob.html
import settings


###--- FUNCTIONS ---###
def count_directories():
    # Use of scandir() to display all the files (excluding directories)
    # in the given path that don’t start with '.';
    # the entry.is_file() call will generally not make an additional system call
    path = settings.DIR_PATH

    files_list = list()

    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                files_list.append(entry)

    print(len(files_list))


###--- DRIVER CODE ---###
if __name__ == "__main__":
    count_directories()


# TO DO: pierce into directoris and count actual files
