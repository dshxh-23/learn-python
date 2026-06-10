import os
from pathlib import Path
import cv2


def _clean_ext(ext):
    """clean extension to ensure the name starts with a dot"""
    return f".{ext.lower().lstrip('.')}"

# -- -- -- -- 

def get_matching_files(target_dir, ext):
    """returns a list of all files in target_dir with extension ext"""
    return [
        # .iterdir() is a generator which returns a Path object for all objects inside the calling directory
        f for f in target_dir.iterdir() if f.suffix.lower() == ext
    ]
    
# -- -- -- --

def convert_img(img_path, from_ext, to_ext):
    img = cv2.imread(img_path)

    if img is None:
        raise FileNotFoundError()   # raise a custom exception, FileNotFoundError is used here temporary

    new_img_path = img_path.with_suffix(to_ext)
    return cv2.imwrite(str(new_img_path), img)

# ---- ---- ---- ----

def batch_convert_images(folder_path, from_ext, to_ext):
    """convert all image files of a specific type to another type inside a path"""

    # formatting ip extensions to ensure valid names
    from_ext = _clean_ext(from_ext)
    to_ext = _clean_ext(to_ext)

    # managing folder_path
    target_dir = Path(folder_path).resolve()

    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: The directory '{target_dir}' does not exist")
        return

    print(f"scanning {target_dir} for {from_ext} files")
    
    matching_files = get_matching_files(target_dir, from_ext)

    if not matching_files:
        print(f"no files found with extension {from_ext}")
        return
    
    print(f"found {len(matching_files)} files. Starting conversion.")
    success_count = 0

    for file_path in matching_files:
        try:
            if convert_img(file_path, from_ext, to_ext):
                print(f"\t[CONVERTED] successfully converted {file_path.name}   -->   {file_path.with_suffix(to_ext).name}")
                success_count += 1
            else:
                print(f"\t [FAILED] could not save {file_path.with_suffix(to_ext).name}")
        except FileNotFoundError:
            print(f"\t[SKIPPED] could not read/parse {file_path.name}")

    print()
    print(f"TASK COMPLETED! Successfully converted {success_count}/{len(matching_files)} from {from_ext} to {to_ext}")


# ====== ====== ====== =======


def main():
    print("===== ===== =====| BATCH IMAGE FORMAT CONVERTER |===== ===== =====")
    print()

    # Optional
    FOLDER_PATH = ""
    FROM_EXT = ""
    TO_EXT = ""

    if not FOLDER_PATH:
        FOLDER_PATH = input("Enter PATH to folder: ").strip()
    
    if not FROM_EXT:
        FROM_EXT = input("Enter the extension to convert FROM: ").strip()

    if not TO_EXT:
        TO_EXT = input("Enter the extension to convert TO: ").strip()
    
    batch_convert_images(FOLDER_PATH, FROM_EXT, TO_EXT)

# -- -- -- --

if __name__ == "__main__":
    main()