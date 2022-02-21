

from Library.Classes.parseBuildData import ParseBuildData
from Library.Classes.build import buildImage
import sys

ParseBuildData.splitSysParams()
print(ParseBuildData.commandParameters)
buildImage = buildImage()
parseJson = ParseBuildData()

buildImage.readJsonFile()
parseJson.parseBuild(buildImage.jsonData['devops'])
print( ParseBuildData.build[0]['builder'])
buildImage.build()

