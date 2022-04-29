"""
    Converts groups of 4 spaces together into tab characters.
"""

# Deps
import os
import sys

# Funcs

def read_file( fp ):
    f = open(fp, "r")
    data = f.read()
    f.close()
    return data

def write_file( fp, data ):
    f = open(fp, "w")
    f.write(data)
    f.close()
    return

def replace_space_with_tabs( data ):
    return data.replace("\t","    ")

if __name__ == "__main__":

    args = sys.argv[1:]
    fp = args[0]

    if len(args) < 1:
        print("[ERROR] Expected at least 1 argument, but 0 were passed.")
    else:
        if os.path.isfile(fp):
            write_file(fp,replace_space_with_tabs(read_file(fp)))
        else:
            print("[ERROR] The provided path is not to a valid file.")
