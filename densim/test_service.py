import sys
from .service import Service

def test_add_service_from_file(fp):
    test_service = Service()
    test_service.add_service_from_file(fp)
    if 1 != test_service.get_number_of_services():
        return False
    test_service.add_service_from_file(fp)
    test_service.add_service_from_file(fp)
    if 1 != test_service.get_number_of_services():
        return False
    return True
    
def test_display_all_services(fp):
    test_service = Service()
    test_service.add_service_from_file(fp)
    test_service.display_all_services()
    return True

def run_all_tests(fp):
    if test_add_service_from_file(fp) == False: return False
    if test_display_all_services(fp) == False: return False

# vim: set et sts=4:
