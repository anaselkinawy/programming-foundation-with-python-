import os
from os import listdir
def rename_file () :
    #getting folders name :-
    file_list = os.listdir("/media/username/partition/prank")
   #getting the directory path
    saved_path = os.getcwd()
    print (saved_path)
    #changing the directory to the file path
    os.chdir("/media/username/partition/prank")

    #rename folders :-
    for file_name in file_list :
        # str.maketrans() that takes the characters-to-delete (the third argument)
        map = str.maketrans("","","1234567890")
        os.rename(file_name,file_name.translate(map))
rename_file()
