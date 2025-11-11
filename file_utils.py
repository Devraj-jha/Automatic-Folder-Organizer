import os 
# this os module is used to manipulate folder and structure of the computer file system.. 
#
import shutil
#used for copying, moving ,  deletintg files, betwen folder easiely.. 
from categories import CATEGORIES

def get_category(file_name):
   

    _ , ext = os.path.splitext(file_name) #. the 2nd line only returns a tuple => ("photo", "jpg")
# the first line is tuple unpacking python let use unpack the thing. 

# _ underscore is. used to ignore a value. 
    ext = ext.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
        return "Others"
    

def organize_folder(folder_path):
    for item in os.listdir(folder_path):
        #returns the list of names. in folder path listdire. meaning I guess. 
        item_path = os.path.join(folder_path, item)

        if os.path.isdir(item_path):
            continue
        
        category = get_category(item)

        category_folder = os.path.join(folder_path, category)
        
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        shutil.move(item_path, os.path.join(category_folder, item))
        print(f"✅ Moved: {item} → {category}/")  # feedback for user


def count_files(folder_path):
   
    total_files = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
    print(f"\nTotal unorganized files before starting: {total_files}")