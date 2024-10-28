import os
import re

# Function to extract numeric prefix, including decimal numbers
def extract_number(name):
    match = re.match(r"(\d+(\.\d+)?)", name)  
    return float(match.group()) if match else float('inf')

# create a root folder for extracted contents
output_root = '0utput-FileContentsExtractor'
os.makedirs(output_root, exist_ok=True)

for root, dirs, files in os.walk('.'):
    if files:
        
        names = [os.path.splitext(name)[0] for name in files]        
        unique_sorted_names = sorted(set(names), key=extract_number)        
        folder_name = os.path.basename(root) if os.path.basename(root) else "root"
        txt_filename = f"{folder_name}_contents.txt"      
        try:
            # Create a subfolder within FileContentsExtractor for each directory
            output_folder = os.path.join(output_root, folder_name)
            os.makedirs(output_folder, exist_ok=True)
            output_path = os.path.join(output_folder, txt_filename)
            with open(output_path, 'w') as f:
                for name in unique_sorted_names:
                    f.write(f"{name}\n")
            print(f"Saved {txt_filename} with {len(unique_sorted_names)} unique names.")
            # print all the unique names in alphabetical order with professional styling 
            print(f"Unique names in alphabetical order:\n{', '.join(unique_sorted_names)}")
        except IOError as e:
            print(f"Error saving {txt_filename}: {e}")