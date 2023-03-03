import os
import shutil

directory = os.curdir

for root, dirs, files in os.walk(directory):
    for name in dirs:
        if name == ".vscode":
            folder_path = os.path.join(root, name)
            print(f"Removing folder: {folder_path}")
            shutil.rmtree(folder_path)
