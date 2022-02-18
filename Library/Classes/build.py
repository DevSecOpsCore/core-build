import json

from Library.Classes.parseBuildData import ParseBuildData


class buildImage:
    jsonData = []

    def __init__(self):
        pass

    @staticmethod
    def readJsonFile(filePath=''):

        with open(filePath+'devops-settings-example.json') as json_file:
            buildImage.jsonData = dict(json.load(json_file))
        return buildImage.jsonData


