import os
 
target_dir = "test"
 
# List all files ending with *.txt.
for (dirpath, dirname, filename) in os.walk(target_dir):
    for file in filename:
        if ".txt" in file:
            print(os.path.join(dirpath, file))