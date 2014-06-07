import json
from pprint import pprint

class ServiceImport:
    """Service class"""

    def __init__(self):
        self.json_version_max = 1

    def import_json(self, filename):
        """Import JSON file"""
        json_data = json.loads(open(filename).read())
        return json_data

# vim: set et sts=4:
