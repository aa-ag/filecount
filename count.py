###--- IMPORTS ---###
import os  # https://docs.python.org/3/library/os.html#os.listdir
# [!] alternatively: glob https://docs.python.org/3/library/glob.html
import settings


###--- FUNCTIONS ---###
def count_directories():
    '''
    - Establishes a path inside a variable, 
    - Creates a list containing the names of the entries 
    in the directory given by path, inside a variable.
    - Prints lenght of that list (number of files in directory)  
    '''
    path = settings.DIR_PATH

    directory_list = os.listdir(path)
    print(directory_list)
    # for this project: ['__pycache__', '.gitignore', 'settings.py', 'count.py']

    number_of_directories = len(directory_list)
    print(number_of_directories)  # for this project: 4


###--- DRIVER CODE ---###
if __name__ == "__main__":
    count_directories()


# TO DO: pierce into directoris and count actual files
