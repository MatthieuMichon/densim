
class Service:
    """Service class"""

    def import_json(self, data):
        """Import JSON data"""
        if data["object"] != "Service":
            raise ValueError("Incorrect JSON object")
        if data["version"] != 1:
            raise ValueError("Incorrect JSON Service version")


# vim: set et sts=4:
