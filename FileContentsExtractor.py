import os
import re
from typing import List, Tuple

def extract_number(name: str) -> float:
    """
    Extracts the leading numeric prefix from a filename.
    
    Args:
        name (str): The filename from which to extract the numeric prefix.
    
    Returns:
        float: The numeric prefix as a float, or infinity if no numeric prefix is found.
    """
    match = re.match(r"(\d+(\.\d+)?)", name)
    return float(match.group()) if match else float('inf')

def get_folder_paths() -> Tuple[str, str]:
    """
    Prompts the user for input and output folder paths.
    
    Returns:
        Tuple[str, str]: A tuple containing the input and output paths.
    """
    folder_path = input("Enter the path of the folder to extract contents from (leave blank for current directory): ")
    folder_path = folder_path if folder_path else '.'
    
    output_root = input("Enter the output path (leave empty to save in the source path): ")
    if not output_root:
        output_root = os.path.join(folder_path, "0utput-FileContentsExtractor")
    os.makedirs(output_root, exist_ok=True)
    
    return folder_path, output_root

def process_folder(root: str, files: List[str], output_folder: str) -> None:
    """
    Processes a folder to extract sorted unique file names and save them to a .txt file.
    
    Args:
        root (str): The root directory containing the files.
        files (List[str]): List of filenames in the folder.
        output_folder (str): The path to save the output .txt file.
    """
    # Remove extensions and keep filenames
    names = [os.path.splitext(name)[0] for name in files]

    # Sort: first by number prefix if present, then alphabetically
    unique_sorted_names = sorted(set(names), key=lambda x: (extract_number(x), x.lower()))

    # Create output filename and path
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

def main() -> None:
    """
    Main function to process the user-specified folder, extracting file names and saving them to .txt files.
    """
    folder_path, output_root = get_folder_paths()

    # Loop through specified folder and subfolders
    for root, dirs, files in os.walk(folder_path):
        if files:  # Only process if there are files in the folder
            relative_path = os.path.relpath(root, folder_path)
            output_folder = os.path.join(output_root, relative_path)
            os.makedirs(output_folder, exist_ok=True)  # Ensure output folder exists

            # Process and save contents of the current folder
            process_folder(root, files, output_folder)

if __name__ == "__main__":
    main()