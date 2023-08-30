import os
import shutil

# 定数として定義
PREFIX = "【設計】"
TARGET_DIRECTORY = "D:\\設計アップロード先"

def rename_and_copy_files(root_directory):
    """
    Rename PDF files in subdirectories with a prefix and then copy them to another drive.
    """
    for current_dir, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith('.pdf'):
                old_path = os.path.join(current_dir, file)
                new_name = PREFIX + file
                new_path = os.path.join(current_dir, new_name)

                # Rename file
                os.rename(old_path, new_path)

                # Prepare the destination directory path
                relative_path = os.path.relpath(current_dir, root_directory)
                destination_folder = os.path.join(TARGET_DIRECTORY, relative_path)
                destination_path = os.path.join(destination_folder, new_name)

                # Create destination folder if not exists
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                # Copy the renamed file
                shutil.copy2(new_path, destination_path)

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))

    rename_and_copy_files(current_directory)
