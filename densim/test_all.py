import sys
from .service import Service
from .service_import import ServiceImport
import densim.test_service
import densim.test_service_import

def add_service():
    test_filename = "data/services/service-4444.json"
    test_data = ServiceImport().import_json(test_filename)
    test_service = Service().import_json(test_data)
    

def main():
    # Unit tests
    densim.test_service.main()
    densim.test_service_import.main()
    # Functionnal tests
    add_service()

if __name__ == "__main__":
    sys.exit(main())

# vim: set et sts=4:
