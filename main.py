# move dxf files to shared dir

# dir 1 C:\Users\Sublimacja_2\Downloads

# dir 2 for placing: C:\Users\Sublimacja_2\Desktop\frez


import os
import time
import subprocess
from scan_folder_script import delete_oldest_files

SRC_DIR = "C:/Users/Sublimacja_2/Downloads"
DEST_DIR = "C:/Users/Sublimacja_2/Desktop/frez"

folder_path = 'C:/Users/Sublimacja_2/Desktop/frez'
max_files = 40

no_files_message_printed = False # Flag to track if the message has been printed

while True:
    # List all .dxf files in the source directory
    dxf_files = [file for file in os.listdir(SRC_DIR) if file.endswith(".dxf")]

    if dxf_files:
        # Get the first .dxf file (you can modify this logic based on your requirements)
        file_to_move = dxf_files[0]
        src_path = os.path.join(SRC_DIR, file_to_move)
        dest_path = os.path.join(DEST_DIR, file_to_move)

        # Check if the file already exists in the destination directory
        if os.path.exists(dest_path):
            print(f"{file_to_move} is already exists in the destination directory. Deleting from source dir.")
            os.remove(src_path)
        else:
            print(f"Moving {file_to_move} to destination folder.")
            subprocess.run(["python", "move_script.py", src_path, dest_path])

        # Reset the flag since there is a file to move
        no_files_message_printed = False
    elif not no_files_message_printed:
        print("No files to move. Standing by...")
        no_files_message_printed = True
    
    
    delete_oldest_files(folder_path, max_files)
    
    time.sleep(1)  # Check every 60 seconds (adjust as needed)
