import os

# Specify the directory path
path = '/Riot Games'

try:
    # Get the list of all files and directories
    dir_contents = os.listdir(path)

    print(f"Contents of '{path}':")
    for item in dir_contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{path}'.")
