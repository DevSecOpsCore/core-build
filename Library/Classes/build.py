import json

from Library.Classes.parseBuildData import ParseBuildData
import subprocess


class buildImage:
    jsonData = []

    def __init__(self):
        pass

    @staticmethod
    def readJsonFile(filePath=''):

        with open(filePath+'devops-settings-example.json') as json_file:
            buildImage.jsonData = dict(json.load(json_file))
        return buildImage.jsonData

    @staticmethod
    def build():

        if ParseBuildData.details[0]["dockerFilePath"] == "":
            ParseBuildData.details[0]["dockerFilePath"] = "./Dockerfile"
        if ParseBuildData.details[0]["dockerFileName"] == "":
            ParseBuildData.details[0]["dockerFileName"] = "Dockerfile"

        if ParseBuildData.build[0]['builder'] == 'podman':
            print ('podman ile build ediyorum.')
            lsYap = subprocess.check_output("echo podman imajlari listeleniyor", shell=True)
            print(lsYap)
    def splitParameters():
        print("sa")

