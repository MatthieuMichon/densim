import json
from pprint import pprint

class Service:
    """Service class"""

    def __init__(self):
        self.service_list = []

    def add_service(self, data):
        "Add service from data"
        # Check for mandatory fields
        if 'code' not in data:
            raise KeyError('lol')
        if data in self.service_list:
            print("Mission already inserted")
            return
        self.service_list.append(data)

    def add_service_from_json(self, jdata):
        """Add service from JSON data"""
        if jdata["object"] != "Service":
            raise ValueError("Incorrect JSON object")
        if jdata["version"] != 1:
            raise ValueError("Incorrect JSON Service version")
        try:
            self.add_service(jdata['data'])
        except Exception:
            raise ValueError("Incorrect JSON Service data")
            
    def add_service_from_file(self, fp):
        """Add service from a JSON data file"""
        try:
            jd = json.loads(open(fp).read())
            self.add_service_from_json(jd)
        except Exception:
            print("Failed to open file: " + fp)

    def get_number_of_services(self):
        return len(self.service_list)

    def display_all_services(self):
        for entry in self.service_list:
            self.display_service(entry)

    def display_service(self, entry):
        """Display a given service"""
        print("Service code: " + str(entry["code"]))
        print(" - Days in service: ", end="")
        for days in entry["days"]:
            print(days + " ", end="")
        print("")
        #pprint(entry)

# vim: set et sts=4:
