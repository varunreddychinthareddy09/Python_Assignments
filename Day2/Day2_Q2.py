import os
def r_and_w_files(source_directory, output_file):
    with open(output_file, "w", encoding="utf-8") as out_file:
        for root, _,files in os.walk(source_directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as in_file:
                        out_file.write(f"--- Content of {file_path} ---\n")
                        out_file.writelines(in_file.readlines())
                        out_file.write("\n\n")
                except Exception as e:
                    print(f"Could not read {file_path}: {e}")

source_directory = r"C:\Users\Varun\Desktop\Python_Assignments"
output_file_path = "c.txt"

r_and_w_files(source_directory, output_file_path)
print(f"All files' contents are written to {output_file_path}")