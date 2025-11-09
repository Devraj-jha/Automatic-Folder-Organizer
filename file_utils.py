import os 
# this os module is used to manipulate folder and structure of the computer file system.. 
#
import shutil
#used for copying, moving ,  deletintg files, betwen folder easiely.. 
from categories import CATEGORIES

def get_category(file_name):
    """
    🧠 Determines the category (folder name) of a given file based on its extension.
    """

    _ , ext = os.path.splitext(file_name) #. the 2nd line only returns a tuple => ("photo", "jpg")
# the first line is tuple unpacking python let use unpack the thing. 

# _ underscore is. used to ignore a value. 
    ext = ext.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
        return "Others"