import json

from Library.Classes.parseBuildData import ParseBuildData
import subprocess


class buildImage:
    jsonData = []

    def __init__(self):
        pass

    @staticmethod
    def readJsonFile():
        with open(ParseBuildData.commandParameters['jPath']+''+ParseBuildData.commandParameters['jName']) as json_file:
            buildImage.jsonData = dict(json.load(json_file))
        return buildImage.jsonData

    @staticmethod
    def build():

        if ParseBuildData.details[0]["dockerFilePath"] == "":
            ParseBuildData.details[0]["dockerFilePath"] = "./Dockerfile"
        if ParseBuildData.details[0]["dockerFileName"] == "":
            ParseBuildData.details[0]["dockerFileName"] = "Dockerfile"

        print ('podman ile build ediliyor.')
        makeBuild = subprocess.check_output("podman build --tag "+ParseBuildData.details[0]["imageName"]+":"+ParseBuildData.details[0]["tag"]
                                            +" -f "+ParseBuildData.details[0]["dockerFilePath"], shell=True)
        print(makeBuild)
        imageList = subprocess.check_output("echo podman imajlari listeleniyor", shell=True)
        print(imageList)
        list = subprocess.check_output("podman images", shell=True)
        print(list)
        loginPodman = subprocess.check_output("podman login " + ParseBuildData.commandParameters['repository']+' -u '+ParseBuildData.commandParameters['username'] +
                                              ' -p '+ParseBuildData.commandParameters['password'], shell=True)
        print (loginPodman)
        imagePush = subprocess.check_output(
            "podman push " + ParseBuildData.details[0]["imageName"]+":"+ParseBuildData.details[0]["tag"]+' ' +
            ParseBuildData.commandParameters['repository']+'/'+ParseBuildData.commandParameters['username']+'/' +
            ParseBuildData.details[0]["imageName"]+":"+ParseBuildData.details[0]["tag"], shell=True)
        print (imagePush)

##podman push myimage quay.io/username/myimage
##sudo buildah push  ${{ inputs.IMAGE_NAME }}:${{ inputs.Repository_Project_version }}  ${{ inputs.USERNAME }}/${{ inputs.Repository_Project_Tag }}:${{ inputs.Repository_Project_version }}
