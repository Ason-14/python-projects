# Python script that reads a folder of uploaded files 
# Prints their file names, file types, and upload status.

from pathlib import Path

def read_uploaded_files(folder_path):
    uploaded_files = Path(folder_path).glob('*')
    
    for file in uploaded_files:
        if file.is_file():
            file_name = file.name
            file_type = file.suffix
            upload_status = "Uploaded"  # Assuming all files in the folder are uploaded
            
            print(f"File Name: {file_name}, File Type: {file_type}, Upload Status: {upload_status}")

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing uploaded files: ")
    read_uploaded_files(folder_path)