import os
import shutil

# directory = os.curdir
directory = r"D:\Projects\Python"

# for root, dirs, files in os.walk(directory):
#     for name in dirs:
#         if name == ".vscode":
#             folder_path = os.path.join(root, name)
#             print(f"Removing folder: {folder_path}")
#             shutil.rmtree(folder_path)


# get all files in directory and then rename them
# for filename in os.listdir(directory):
#     filename_path = os.path.join(directory, filename)
#     extension = os.path.splitext(filename)[1]
#     new_filename = filename.replace(".FilmKio", "") + extension
#     new_filename_path = os.path.join(directory, new_filename)
#     shutil.move(filename_path, new_filename_path)

number = 9
for file in os.listdir(directory):
    if file.startswith(str(number).zfill(2)):
        shutil.move(os.path.join(directory, file),
                    os.path.join(directory, file.replace(str(number).zfill(2), str(number - 1).zfill(2))))
        number += 1
