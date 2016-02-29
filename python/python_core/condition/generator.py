import os

def walk(path):
    if os.path.isdir(path):
        for file in os.listdir(path):
            file_path=os.path.join(path, file);
            for sub_file in walk(file_path):
                yield sub_file
    else:
        yield path


for file in walk("."):
    print file
