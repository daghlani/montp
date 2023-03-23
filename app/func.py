from genericpath import isfile
from flask import url_for
from os import listdir

def compile_javascript():
    # Defining the path to the folder where the JS files are saved
    path = 'static/js'
    # Getting all the files from that folder
    files = [f for f in listdir(path) if isfile('/'.join([path, f]))]
    # Setting an iterator
    i = 0
    # Looping through the files in the first folder
    all_js_files = list()
    for file in files:
        # Building a file name
        file_name = "js/" + file
        # Creating a URL and saving it to a list
        all_js_files.append(url_for('static', filename = file_name))
        # Updating list index before moving on to next file
        i +=1
    return(all_js_files)