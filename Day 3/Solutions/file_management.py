import shutil
import tempfile
import glob
import os

# File I/O operations
def file_io_operations():
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    try:
        # Write to the file
        with open(temp_file.name, 'w') as file:
            file.write("Hello, Salesforce!")
        
        # Read from the file
        with open(temp_file.name, 'r') as file:
            content = file.read()
            print("File Content:", content)
    finally:
        # Delete the temporary file
        os.unlink(temp_file.name)

# File management with shutil and glob
def file_management():
    # Create a directory and some files
    os.makedirs("example_dir", exist_ok=True)
    for i in range(3):
        with open(f"example_dir/file_{i}.txt", 'w') as file:
            file.write(f"File {i}")
    
    # Copy files
    shutil.copy("example_dir/file_0.txt", "example_dir/file_0_copy.txt")
    
    # List files
    print("Files in example_dir:", glob.glob("example_dir/*.txt"))
    
    # Clean up
    shutil.rmtree("example_dir")

def main():
    file_io_operations()
    file_management()

if __name__ == "__main__":
    main()
