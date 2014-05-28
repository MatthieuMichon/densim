import json

class Mission:
    """Mission class"""

    def __init__(self):
        """Default constructor"""

    def __init__(self, mission_json_filename):
        """Constructor with JSON filename"""
        self.json_filename = mission_json_filename


    def set_filename(self, mission_json_filename):
        """Return the JSON filename"""
        self.json_filename = mission_json_filename
    
    def get_filename(self):
        """Return the JSON filename"""
        return self.json_filename


    def get_file_json_contents(self):
        """Return JSON contents of the selected file"""
        return self.json_data

# vim: set et sts=4:
