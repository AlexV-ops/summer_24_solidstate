import os
from datetime import datetime
import shutil

def convert_and_move_files(directory, source_ext, target_ext):
    # Create new folders
    current_date = datetime.now().strftime("%d%b%y")
    xy_folder = os.path.join(directory, f"XY_{current_date}")
    x_y_folder = os.path.join(directory, f"X_Y_{current_date}")
    
    os.makedirs(xy_folder, exist_ok=True)
    os.makedirs(x_y_folder, exist_ok=True)
    
    # Convert and move files
    for filename in os.listdir(directory):
        if filename.endswith(source_ext):
            source_path = os.path.join(directory, filename)
            new_filename = filename[:-len(source_ext)] + target_ext
            
            if target_ext == '.xy':
                target_path = os.path.join(xy_folder, new_filename)
                shutil.copy2(source_path, target_path)
                shutil.move(source_path, os.path.join(x_y_folder, filename))
            else:
                target_path = os.path.join(x_y_folder, new_filename)
                shutil.copy2(source_path, target_path)
                shutil.move(source_path, os.path.join(xy_folder, filename))
            
            print(f"Converted and moved: {filename} -> {new_filename}")

def main():
    directory = input("Enter the directory path: ")
    
    if not os.path.isdir(directory):
        print("Invalid directory path.")
        return
    
    choice = input("Choose conversion (1 for .xy to .x_y, 2 for .x_y to .xy): ")
    
    if choice == '1':
        convert_and_move_files(directory, '.xy', '.x_y')
    elif choice == '2':
        convert_and_move_files(directory, '.x_y', '.xy')
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
