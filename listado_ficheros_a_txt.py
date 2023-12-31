# Script for listing files and subfolders.
# Generates a txt file as output.
# Uses arguments from terminal command line.

import argparse
import os

# Definition of argparse object

parser = argparse.ArgumentParser(
    prog = "listado_ficheros_a_txt.py",
    description = "Lists files and subfolders in a txt output file",
    epilog = "Texto al final de la ayuda"
    )
parser.add_argument("input_folder", help = "Folder (and path) to be listed")
parser.add_argument("output_file", help = "Filename to be written")
args = parser.parse_args()

# Generates the output file
output_txt_filename = args.output_file + ".txt"
output_txt_file = open(r"{}".format(output_txt_filename), "w")
print("Generating file.")
for folder_name, subfolders, filenames in os.walk(args.input_folder):
    output_txt_file.write(folder_name + "\n")
    for subfolder in subfolders:
        output_txt_file.write(subfolder + "\n")
    for filename in filenames:
        output_txt_file.write(filename + "\n")
    output_txt_file.write("\n")
print("Done.")
print(f"List saved in file \"{output_txt_filename}\" in folder \"{os.getcwd()}\"")

# Closes the written file
output_txt_file.close()








######################################

# import os
# import re

# def path_validation(path):
#     """
#     Assesses the input from the user looking for a path; checks if the path really exists
#     """
#     matched_path = re.match(r"^([a-z]:)(((\\*|\/*)[a-z\s0-9^&'@{}\[\],$=!\-#\(\)%\.\+~_]+)*(\\*|\/*))", path, re.IGNORECASE)
#     if matched_path != None:
#         # match_path.group() returns the matched part as a string
#         return os.path.isdir(matched_path.group()), matched_path.group()
#     else:
#         return False, None

# # Input from user and validate
# while True:
#     path = input("Which folder do you want to list? (Input a valid absolute path like this C:\XXXXX\YYYYY\ZZZZZ): ")
#     validation, matched_path = path_validation(path)
#     if validation:
#         break

# # Generates the output file once everything is valid
# output_txt_file = open("output_txt_file.txt", "w")
# print("Generating file.")
# for folder_name, subfolders, filenames in os.walk(r"{}".format(matched_path)):
#     output_txt_file.write(folder_name + "\n")
#     for subfolder in subfolders:
#         output_txt_file.write(subfolder + "\n")
#     for filename in filenames:
#         output_txt_file.write(filename + "\n")
#     output_txt_file.write("\n")
# print("Done.")
# print(f"List saved in file \"output_txt_file.txt\" in folder \"{os.getcwd()}\"")

# # Closes the written file
# output_txt_file.close()






# ####################################################
# # Script for listing files and subfolders.
# # Generates a txt file as output.
# # Uses arguments from terminal command line.

# import sys, getopt

# def main(argv):
#     inputfile = ""
#     outputfile = ""
#     try:
#         opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
#     except getopt.GetoptError:
#         print ("listado_ficheros_a_txt.py -i <inputpath> -o <outputfile>")
#         sys.exit(2)
#     for opt, arg in opts:
#         if opt == '-h':
#             print ('test.py -i <inputfile> -o <outputfile>')
#             sys.exit()
#         elif opt in ("-i", "--ifile"):
#             inputfile = arg
#         elif opt in ("-o", "--ofile"):
#             outputfile = arg
#     print ('Input file is ', inputfile)
#     print ('Output file is ', outputfile)

# if __name__ == "__main__":
#     main(sys.argv[1:])