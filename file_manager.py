# Parser class
# Parses the given JSON file

import json

class FileManager:
    # Called on object instantiation
    def __init__(self):
        pass

    # Parses the json file and returns the data as text
    def parse_json(self, file):
        # read file contents
        with open(file, 'r') as json_file:
            pure_json = json_file.read()
        json_file.close()

        return json.loads(pure_json)