import sys
import shutil

def move_file(src_path, dest_path):
    try:
        shutil.move(src_path, dest_path)
        print(f"Moved {src_path} to {dest_path}")
    except Exception as e:
        print(f"Error moving {src_path} to {dest_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python move_script.py <source_path> <destination_path>")
        sys.exit(1)

    source_path = sys.argv[1]
    destination_path = sys.argv[2]

    move_file(source_path, destination_path)
