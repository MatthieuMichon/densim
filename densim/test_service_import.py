import sys
from densim.service_import import ServiceImport

def test_import_json(test_filename = "data/services/service-4444.json"):
    test_service = ServiceImport()
    test_service.import_json(test_filename)

def main():
    return test_import_json()

if __name__ == "__main__":
    sys.exit(main())

# vim: set et sts=4:
