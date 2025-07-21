import os
file_path = "delete.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} has been deleted.")
else:
    print("File does not exist.")
