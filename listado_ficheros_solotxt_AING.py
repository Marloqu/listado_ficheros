# Script for listing files and subfolders.
# Generates a txt files as output.

import os
import re

def path_validation(path):
    """
    Assesses the input from the user looking for a path; checks if the path really exists
    """
    matched_path = re.match(r"^([a-z]:)(((\\*|\/*)[a-z\s0-9^&'@{}\[\],$=!\-#\(\)%\.\+~_]+)*(\\*|\/*))", path, re.IGNORECASE)
    if matched_path != None:
        # match_path.group() returns the matched part as a string
        return os.path.isdir(matched_path.group()), matched_path.group()
    else:
        return False, None

# Input from user and validate
while True:
    path = input("Which folder do you want to list? (Input a valid absolute path like this C:\XXXXX\YYYYY\ZZZZZ): ")
    validation, matched_path = path_validation(path)
    if validation:
        break

# Generates the output file once everything is valid
output_txt_file = open("output_txt_file.txt", "w")
print("Generating file.")
for folder_name, subfolders, filenames in os.walk(r"{}".format(matched_path)):
    output_txt_file.write(folder_name + "\n")
    for subfolder in subfolders:
        output_txt_file.write(subfolder + "\n")
    for filename in filenames:
        output_txt_file.write(filename + "\n")
    output_txt_file.write("\n")
print("Done.")
print(f"List saved in file \"output_txt_file.txt\" in folder \"{os.getcwd()}\"")

# Closes the written file
output_txt_file.close()
