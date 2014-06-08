import sys
from .test_service import test_add_service_from_file

def main():
    test_filename = "data/services/service-4444.json"
    if test_add_service_from_file(test_filename) != True:
        return False
    return True

if __name__ == "__main__":
    sys.exit(main())

# vim: set et sts=4:
