import os
import datetime



def get_creation_date(file_path):

    # Get the creation time of the file
    creation_time = os.path.getctime(file_path)

    # Convert the timestamp to a datetime object
    return datetime.datetime.fromtimestamp(creation_time)


def delete_oldest_files(folder_path, max_files):
    files_info = []
    
    # Iterate over files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        # Check if the path is a file (not a folder)
        if os.path.isfile(file_path):
            # Get the creation date of the file
            creation_date = get_creation_date(file_path)
            # Add file info to list
            files_info.append((file_path, creation_date))
    
    # Sort files by creation date (oldest first)
    files_info.sort(key=lambda x: x[1])
    
    # Calculate the number of files to delete
    num_files_to_delete = len(files_info) - max_files
    
    if num_files_to_delete > 0:
        # Delete the oldest files
        for i in range(num_files_to_delete):
            os.remove(files_info[i][0])
            print("Deleted:", files_info[i][0])
    else:
        return
        

# Example usage:



"""
target_dir = "C:/Users/Sublimacja_2/Desktop/frez"
max_files = 20

def get_creation_time(file_path):
    file_name = 
    file_path = os.path.join(target_dir, file_name)
    creation_time = os.path.getctime(file_path)
    return creation_time
"""

"""
def delete_oldest_files(target_dir, max_files):
    files = os.listdir(target_dir)

    if len(files) > max_files:
        files_with_times = [
            (file_name, get_creation_time(os.path.join(target_dir, file_name)))
            for file_name in files
        ]
        files_with_times.sort(key=lambda x: x[1]) 
        files_to_delete = files_with_times[len(files) - max_files]
        for file_name, _ in files_to_delete:
            os.remove(os.path.join(target_dir, file_name))
            print("Deleting file: {file_name}")

"""