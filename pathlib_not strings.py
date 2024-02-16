import pathlib

path = pathlib.Path(('data') / ('Results.csv'))

from pathlib import Path
path = Path('/path/to/directory')



# Joining paths
p = Path('/home/user')
q = p / 'Documents'  # Path('/home/user/Documents')

# Accessing path components
p = Path('/home/user/Documents/file.txt')
p.name  # 'file.txt'
p.parent  # Path('/home/user/Documents')

# Checking path existence
p = Path('/home/user/Documents/file.txt')
p.exists()  # True or False

# Creating a new directory
p = Path('/home/user/new_directory')
p.mkdir()

# Renaming a file
p = Path('/home/user/Documents/old_name.txt')
p.rename('/home/user/Documents/new_name.txt')

# Deleting a file
p = Path('/home/user/Documents/unwanted_file.txt')
p.unlink()

# Iterating over a directory
p = Path('/home/user/Documents')
for child in p.iterdir():
    print(child)

# Filtering files based on specific criteria
txt_files = list(p.glob('*.txt'))

# Performing batch operations
for txt_file in txt_files:
    txt_file.unlink()

# Retrieving file size
p = Path('/home/user/Documents/file.txt')
p.stat().st_size  # size in bytes

# Retrieving creation/modification timestamps
p.stat().st_ctime  # creation time
p.stat().st_mtime  # modification time

# Retrieving permissions
p.stat().st_mode  # permissions

# Reading file content
p = Path('/home/user/Documents/file.txt')
content = p.read_text()

# Writing to a file
p.write_text('Hello, world!')

# File Access Modes
with new_file.open(mode="a") as file:
    file.write("Appended text")

# Pattern matching
p = Path('/home/user/Documents/file.txt')
p.match('*.txt')  # True

# Globbing
p = Path('/home/user/Documents')
for txt_file in p.glob('*.txt'):
    print(txt_file)

# Recursive operations
for txt_file in p.rglob('*.txt'):
    print(txt_file)

# Pattern Matching and Globbing
pattern_match = path / "*.txt"
txt_files = list(path.glob(pattern_match))

# Recursive Operations
all_files = list(path.rglob("*"))

# Searching for Files
files_to_find = path.rglob("*.log")


with Path("/path/to/file.txt").open() as file:
    content = file.read()
    # Perform operations on the file

# File is automatically closed outside the 'with' block


directory = Path("/path/to/files")

# Batch rename all files with "old_" prefix
for file in directory.glob("old_*"):
    new_name = file.name.replace("old_", "")
    file.rename(directory / new_name)


from pathlib import Path
import shutil

source_file = Path("/path/to/source/file.txt")
destination = Path("/path/to/destination/")

# Copy the file
shutil.copy(source_file, destination)

# Move the file
shutil.move(source_file, destination)



directory = Path("/root/directory")

# Find all Python files in the directory tree
python_files = list(directory.rglob("*.py"))

# Print the results
for file in python_files:
    print(file)


# Correct
with new_file.open(mode="w") as file:
    file.write("Content")

# Avoid
with open(str(new_file), mode="w") as file:
    file.write("Content")



