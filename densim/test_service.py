import sys
from .service import Service

def test_add_service_from_file(fp):
    test_service = Service()
    test_service.add_service_from_file(fp)
    if 1 != test_service.get_number_of_services():
        return False
    test_service.add_service_from_file(fp)
    test_service.add_service_from_file(fp)
    if 3 != test_service.get_number_of_services():
        return False
    return True
    

def main():
    return test_add_service_from_file()

if __name__ == "__main__":
    sys.exit(main())

# vim: set et sts=4:
