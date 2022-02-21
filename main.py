

from Library.Classes.parseBuildData import ParseBuildData
from Library.Classes.build import buildImage
import sys

ParseBuildData.splitSysParams()

buildImage = buildImage()
parseJson = ParseBuildData()
buildImage.readJsonFile()
parseJson.parseBuild(buildImage.jsonData['devops'])
buildImage.build()

