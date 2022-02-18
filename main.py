

from Library.Classes.parseBuildData import ParseBuildData
from Library.Classes.build import buildImage


buildImage = buildImage()
parseJson = ParseBuildData()
buildImage.readJsonFile()
parseJson.parseBuild(buildImage.jsonData['devops'])

print (parseJson.details)