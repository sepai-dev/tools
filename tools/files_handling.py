import os

def find_files_by_extension(base_path, file_extension):
    assert os.path.isdir(base_path), f"The path {base_path} does not exist or is not a directory."

    files = []
    for root, _, filenames in os.walk(base_path):
        for filename in filenames:
            if filename.endswith(file_extension):
                relative_path = os.path.relpath(os.path.join(root, filename), base_path)
                files.append(relative_path)
    return files
