import json
from pprint import pprint

class Service:
    """Service class"""

    def __init__(self):
        self.service_list = []

    def add_service(self, data):
        "Add service from data"
        self.service_list.append(data)

    def add_service_from_json(self, jdata):
        """Add service from JSON data"""
        if jdata["object"] != "Service":
            raise ValueError("Incorrect JSON object")
        if jdata["version"] != 1:
            raise ValueError("Incorrect JSON Service version")
        try:
            self.add_service(jdata['data'])
        except Error:
            raise ValueError("Incorrect JSON Service data")
            
    def add_service_from_file(self, fp):
        """Add service from a JSON data file"""
        jd = json.loads(open(fp).read())
        self.add_service_from_json(jd)

    def get_number_of_services(self):
        return len(self.service_list)

# vim: set et sts=4:
