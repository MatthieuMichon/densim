import sys
from .test_service import run_all_tests

def main():
    test_filename = "data/services/service-4444.json"
    if run_all_tests(test_filename) != True:
        return False
    return True

if __name__ == "__main__":
    sys.exit(main())

