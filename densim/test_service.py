import sys
from .service import Service

def test_import_json():
    test_data = {'object': 'Service', 'version': 1}
    test_service = Service()
    test_service.import_json(test_data)

def main():
    return test_import_json()

if __name__ == "__main__":
    sys.exit(main())

# vim: set et sts=4:
