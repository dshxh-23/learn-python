import sys
from pathlib import Path
import csv

# --------

def get_path() -> str:
    """
    Get path to required directory from the user
    
    Returns:
        Path: the directory path as a pathlib.Path object
    
    Raises:
        ValueError: if directory path does not exist

    """
    if len(sys.argv) == 2:
        directory_path = Path(sys.argv[1])
    elif len(sys.argv) == 1:
        directory_path = Path(input("Enter directory path: ").strip())
    else:
        sys.exit("Too many command-line arguments")

    if not directory_path.is_dir():
        raise ValueError(f"No directory at {directory_path}")
    
    return directory_path

# -- -- -- --

def get_file_size(file: str):
    """
    get file size rounded to 2 decimal places in KB

    Args:
        file (str): path to required file.

    Returns:
        str: the file size (in KB) rounded to 2 decimal places.
    """
    return f"{round(Path(file).stat().st_size) / 1024: .2f} KB"

# -- -- -- --

def get_folder_size():
    ...

# -- -- -- --

def format_size():
    ...

# -- -- -- --

def analyze_directory():
    ...

# -- -- -- --

def export_to_csv(data):
    op_path = Path(__file__).resolve().parent / "directory_analysis.csv"
    with open(
        op_path, 
        mode='w', 
        newline='',
        encoding='utf-8'
    ) as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=["File Name", "File Size"])
        writer.writeheader()
        for row in data: writer.writerow(row)

# -- -- -- --

def print_summary():
    ...

# ==== ==== ==== ====

def main():
    try:
        dir_path = get_path()
    except ValueError as e:
        print(f"[!] VALUE ERROR: {e}")
        sys.exit()

    data = []
    files = [f for f in dir_path.iterdir() if f.is_file()]

    for f in files:
        data.append({"File Name" : f.name, "File Size" : get_file_size(f)})

    export_to_csv(data)
    
# -- -- -- --

if __name__ == "__main__":
    main()