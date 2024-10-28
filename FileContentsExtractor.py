import os
import re

# Function to extract numeric prefix, including decimal numbers
def extract_number(name):
    match = re.match(r"(\d+(\.\d+)?)", name)  
    return float(match.group()) if match else float('inf')

for root, dirs, files in os.walk('.'):
    if files:
        names = [os.path.splitext(name)[0] for name in files]        
        unique_sorted_names = sorted(set(names), key=extract_number)        
        folder_name = os.path.basename(root) if os.path.basename(root) else "root"
        txt_filename = f"{folder_name}_contents.txt"        
        try:
            with open(txt_filename, 'w') as f:
                for name in unique_sorted_names:
                    f.write(f"{name}\n")
            print(f"Saved {txt_filename} with {len(unique_sorted_names)} unique names.")
        except IOError as e:
            print(f"Error saving {txt_filename}: {e}")