# Script for listing files and subfolders.
# Generates a TXT or XLSX file as output.
# Uses arguments from terminal command line.

import argparse
import os
import openpyxl

# Definition of argparse object

parser = argparse.ArgumentParser(
    prog = "listado_ficheros.py",
    description = "Lists files and subfolders from a folder into a .txt or .xlsx output file",
    epilog = "Texto al final de la ayuda"
    )
group = parser.add_mutually_exclusive_group()
parser.add_argument("input_folder", help = "Folder (and path) to be listed")
parser.add_argument("output_file", help = "Filename to be written")
group.add_argument("-txt", "--txt", help = "txt file type", action = "store_true")
group.add_argument("-xlsx", "--xlsx", help = "xlsx file type", action = "store_true")
args = parser.parse_args()

# Generates the output file

if args.txt:
    output_filename = args.output_file + ".txt"
    output_file_object = open(r"{}".format(output_filename), "w")
    print("Generating file.")
    for folder_name, subfolders, filenames in os.walk(args.input_folder):
        output_file_object.write(folder_name + "\n")
        for subfolder in subfolders:
            output_file_object.write(subfolder + "\n")
        for filename in filenames:
            output_file_object.write(filename + "\n")
        output_file_object.write("\n")
    print("Done.")
    print(f"List saved in file \"{output_filename}\" in folder \"{os.getcwd()}\"")
else:
    output_filename = args.output_file + ".xlsx"
    output_file_object = open(r"{}".format(output_filename), "w")
    print("Generating file.")
    for folder_name, subfolders, filenames in os.walk(args.input_folder):
        output_file_object.write(folder_name + "\n")
        for subfolder in subfolders:
            output_file_object.write(subfolder + "\n")
        for filename in filenames:
            output_file_object.write(filename + "\n")
        output_file_object.write("\n")
    print("Done.")
    print(f"List saved in file \"{output_filename}\" in folder \"{os.getcwd()}\"")    

# Closes the written file
output_file_object.close()








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
# output_file_object = open("output_file_object.txt", "w")
# print("Generating file.")
# for folder_name, subfolders, filenames in os.walk(r"{}".format(matched_path)):
#     output_file_object.write(folder_name + "\n")
#     for subfolder in subfolders:
#         output_file_object.write(subfolder + "\n")
#     for filename in filenames:
#         output_file_object.write(filename + "\n")
#     output_file_object.write("\n")
# print("Done.")
# print(f"List saved in file \"output_file_object.txt\" in folder \"{os.getcwd()}\"")

# # Closes the written file
# output_file_object.close()






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