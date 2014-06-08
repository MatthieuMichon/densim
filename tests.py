import sys

from data.check_tests_data import are_files_json_compliant
import densim.test_all

def main():
    json_ok = are_files_json_compliant('.')
    if json_ok != 0:
        raise Exception
    if densim.test_all.main() != True:
        return -1
    return 0

if __name__ == '__main__':
    sys.exit(main())

# vim: set et sts=4:
