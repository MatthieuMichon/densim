# Check all JSON files located under this directory including sub-directory

import json
import os

def is_file_json_compliant(filename):
    """Check if the file given in argument contains a valid JSON object"""
    print("File: "+filename+" ... ", end="")
    try:
        json_data = json.load(open(filename))
    except Exception:
        print("bad.")
        return False
    print("OK.")
    return True

def are_files_json_compliant(directory):
    """Check if all the JSON files in the given directory are correct"""
    status = False
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if (filename[-5:]=='.json'):
                json_filename = os.path.join(root, filename)
                status = is_file_json_compliant(json_filename)
                if (status != True):
                    return -1
    if (status != True):
        return -1
    return 0

if __name__ == '__main__':
    json_ok = are_files_json_compliant('.')
    if (json_ok == 0):
        exit(0)
    exit(-1)

# vim: set et sw=4 sts=4:
