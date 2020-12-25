###--- IMPORTS ---###
import os  # https://docs.python.org/3/library/os.html#os.listdir
# [!] alternatively: glob https://docs.python.org/3/library/glob.html
import settings


###--- FUNCTIONS ---###
def count_files():
    '''
    - Establishes a path inside a variable, 
    - Creates a list containing the names of the entries 
    in the directory given by path, inside a variable.
    - Prints lenght of that list (number of files in directory)  
    '''
    path = settings.DIR_PATH

    file_list = os.listdir(path)
    print(file_list)
    # for this project: ['__pycache__', '.gitignore', 'settings.py', 'count.py']

    number_of_files = len(file_list)
    print(number_of_files)  # for this project: 4


###--- DRIVER CODE ---###
if __name__ == "__main__":
    count_files()
