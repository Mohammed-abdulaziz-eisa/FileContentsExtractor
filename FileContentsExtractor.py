import os
import re

# Function to extract numeric prefix, including decimal numbers
def extract_number(name):
    match = re.match(r"(\d+(\.\d+)?)", name)  
    return float(match.group()) if match else float('inf')

# Ask user to specify a folder path to process
folder_path = input("Enter the path to the folder to extract contents from (leave blank for current directory): ") or os.getcwd()

# create a root folder for extracted contents
output_root = '0utput-FileContentsExtractor'
os.makedirs(output_root, exist_ok=True)

for root, dirs, files in os.walk(folder_path):
    if files:
        
        names = [os.path.splitext(name)[0] for name in files]        
        unique_sorted_names = sorted(set(names), key=extract_number)        
        
        # Determine output folder and file names 
        relative_path = os.path.relpath(root, folder_path)
        output_folder = os.path.join(output_root, relative_path)
        os.makedirs(output_folder, exist_ok=True)
        txt_filename = f"{os.path.basename(root)}_contents.txt"
        output_path = os.path.join(output_folder, txt_filename)
        
        # Save the sorted unique names to a .txt file
        try:
            with open(output_path, 'w') as f:
                for name in unique_sorted_names:
                    f.write(f"{name}\n")
            print(f"Saved {output_path} with {len(unique_sorted_names)} unique names.")
        except IOError as e:
            print(f"Error saving {output_path}: {e}")

        # Display unique names in alphabetical order with styling
        print(f"Unique names in alphabetical order in '{output_path}':")
        print(", ".join(unique_sorted_names))
        