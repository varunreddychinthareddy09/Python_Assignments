import os
def find_largest_file(directory):
    maximum_of_size = 0
    largest_file = None
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size > maximum_of_size:
                maximum_of_size = file_size
                largest_file = file_path
    return largest_file, maximum_of_size

directory_path = r"C:\Users\Varun\Desktop"
file_name, file_size = find_largest_file(directory_path)
print (f"The largest file is: {file_name}")
print(f"Size: {file_size} bytes")