###
### This script renames files in a given directory to prepare them to be served
### by a web server. It does the following:
### 1. Takes a directory name as an argument. It assumes the directory is in /static/data.
### 2. Checks if the directory exists.
### 3. Renames files in the directory by:
###    - Replacing spaces and underscores with dashes
###    - Lowercase the file names
###    - Replacing Romanian characters with English characters
###    - Removing the lesson number from the file name
###    - Trimming leading dashes
### 4. Prints the old and new file names.
###
### Usage:
### python folder_transformer.py <directory_name>
###

import os

# get current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
# goto static/data/<arg1>
# get the first argument from the command line
arg1 = os.sys.argv[1]
directory = os.path.join(current_directory, 'static', 'data', arg1)
# check if the directory exists
if not os.path.exists(directory) or not os.path.isdir(directory):
    print(f"Directory {directory} does not exist")
    exit(1)

# get all files in the directory
files = os.listdir(directory)

# extract lesson number from the directory
lesson_number = arg1.split('-')[0]
# edit the file names to exclude the lesson number
for file in files:
    # replace spaces and underscores with dashes
    new_file_name = file.replace(' ', '-').replace('_', '-')
    # lowercase the file name
    new_file_name = new_file_name.lower()
    # replace roumanian characters with english characters
    new_file_name = new_file_name.replace('ă', 'a').replace('â', 'a').replace('î', 'i').replace('ș', 's').replace('ț', 't')
    # check if the file name starts with the lesson number
    if file.startswith(lesson_number):
        # remove the lesson number from the file name and trim start
        new_file_name = new_file_name.replace(lesson_number, '').lstrip('-')
    else:
        print(f"File {file} does not start with lesson number {lesson_number}")
    os.rename(os.path.join(directory, file), os.path.join(directory, new_file_name))
    print(f"Renamed {file} to {new_file_name}")