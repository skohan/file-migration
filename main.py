#!/bin/bash

import os
import shutil
import datetime

# Define the root directory containing the files to be organized
root_dir = './test'

# Loop through all files and directories in the root directory and its subdirectories
for subdir, dirs, files in os.walk(root_dir):
    
    # print(subdir)

    no_of_files = len(files)
    for file in files:
        # Get the creation time of the file
        file_path = os.path.join(subdir, file)
        creation_time = os.path.getctime(file_path)
        creation_datetime = datetime.datetime.fromtimestamp(creation_time)
        
        # Create year/month/day subdirectories based on the creation time of the file

        year_dir = os.path.join(root_dir, str(creation_datetime.year))
        if not os.path.exists(year_dir):
            os.mkdir(year_dir)

        month_dir = os.path.join(year_dir, str(creation_datetime.month).zfill(2))
        if not os.path.exists(month_dir):
            os.mkdir(month_dir)

        day_dir = os.path.join(month_dir, str(creation_datetime.day).zfill(2))
        if not os.path.exists(day_dir):
            os.mkdir(day_dir)
        
        # Move the file to its corresponding year/month/day subdirectory
        new_file_path = os.path.join(day_dir, file)
        shutil.move(file_path, new_file_path)

    print(f"Total {no_of_files} moved.")
