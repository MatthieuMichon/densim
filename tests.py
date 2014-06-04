from data.check_tests_data import *

if __name__ == '__main__':
    json_ok = are_files_json_compliant('.')
    if (json_ok == 0):
        exit(0)
    exit(-1)
