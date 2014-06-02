import json
from glob import glob

def check_test_json():
    try:
        json_data = json.load(open("tests/data/mission-kyoto-4444.json"))
    except Exception:
        print("Fail!")
        return False
    print("OK")
    return True

def is_file_json_compliant(filename):
    try:
        json_data = json.load(open(filename))
    except Exception:
        print("Failed")
        return False
    print("OK")
    return True

def check_all_json_per_directory(directory):
    """Checks all JSON files in the given directory"""
    pathname = directory + '/*.json'
    for filename in glob(pathname):
        print(""+filename+': ', end = "")
        with open(filename) as fp:
            rc = is_file_json_compliant(filename)
            if (rc != True):
                return -1
    return 0

if __name__ == '__main__':
    json_ok = check_all_json_per_directory("tests/data")
    if (json_ok == 0):
        exit(0)
    exit(-1)

# vim: set et sts=4:
