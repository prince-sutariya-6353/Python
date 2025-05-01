import os

folder_path = r'/prince'  #your folder path

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):  # Make sure it's a file (not a folder)
        os.remove(file_path)
        print(f"Deleted: {file_path}")
