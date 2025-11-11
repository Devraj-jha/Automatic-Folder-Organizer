import os 
from file_utils import organize_folder , count_files 

def main():
    
    folder_path = input("Enter the full path of the folder!!: ")

    if not os.path.exists(folder_path):
        print("folder path Don't exist !! ")
        return 
    
    count_files(folder_path)
    organize_folder(folder_path)

    print("Folder organization complete! ")


if __name__ == "__main__":
    main()
