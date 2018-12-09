# Calculate Size of Folders in a Directory

# Takes 1 argument: directory path
# Returns all folders and corresponding sizes in GB for given directory
# Does not return folders whose size is less than 1 MB

import os
import sys

total_size = 0

folder_sizes = {}
try:
    start_dir = sys.argv[1]
except:
    sys.exit('\nPlease specify the directory as an argument.')

try:
    os.chdir(start_dir)
except:
    sys.exit('\nInvalid directory name.')

for folder in os.listdir(start_dir):
    total_size = 0;
    start_path = os.path.join(start_dir,folder)
    for path, dirs, files in os.walk(start_path):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)

    if total_size >= 1000000:
        folder_sizes[folder] = total_size/1000000000

for item in folder_sizes:
    print("{}: {:.3f} GB".format(item, folder_sizes[item]))
