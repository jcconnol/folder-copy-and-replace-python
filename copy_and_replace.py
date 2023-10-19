import shutil
import os
import fileinput
import sys

source_folder = os.getcwd() + "\\template\\"
destination_folder = os.getcwd() + "\\output\\"

def copy_folder():
    try:
        shutil.copytree(source_folder, destination_folder)
        print(f"Current directory '{source_folder}' copied to '{destination_folder}' successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def replace_text_in_files(directory, old_text, new_text):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                try:
                    with fileinput.FileInput(file_path, inplace=True) as file:
                        for line in file:
                            print(line.replace(old_text, new_text), end='')
                except Exception as e:
                    print(f"Error processing file {file_path}: {str(e)}")

def replace_text_in_filenames(directory, old_text, new_text):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if old_text in filename:
                old_path = os.path.join(root, filename)
                new_filename = filename.replace(old_text, new_text)
                new_path = os.path.join(root, new_filename)
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed '{old_path}' to '{new_path}'")
                except Exception as e:
                    print(f"Error renaming file '{old_path}': {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py new_text")
        sys.exit(1)

    new_text = sys.argv[1]

    copy_folder()

    replace_text_in_files(destination_folder, "placeholder-text", new_text)

    replace_text_in_filenames(destination_folder, "placeholder-text", new_text)
