import os
import glob
import json
from pprint import pprint

class Station:
    """Station class"""

class Line:
    """Line class"""

class Railmap:
    """Railmap class"""

    def __init__(self, name = "default"):
        self.name = name

    def import_file(self, filename):
        try:
            json_data = json.loads(open(filename).read())
            if json_data["object"] not in self.railmap_objects:
                # not a relavent JSON file
                return
        except Exception:
            print("JSON format error")

    def import_folder(self, fp):
        for filename in glob.glob(os.path.join(fp, '*.json')):
            self.import_file(filename)

    railmap_objects = {"Service": Line, "Station": Station}

if __name__ == '__main__':
    railmap = Railmap("Hankyu-2014")
    railmap.import_folder("data/services")

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
        print(" - Events: ")
        for event in entry["events"]:
            self.display_event(event)
        print("")

	# TODO: Move in new file event.py
    def display_event(self, event):
        """Display a given event"""
        time = event['time']
        station = event['station']
        action = event['action']
        event = Event(time, station, action)
        event.display()

