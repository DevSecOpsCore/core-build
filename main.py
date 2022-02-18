

from Library.Classes.parseBuildData import ParseBuildData
from Library.Classes.build import buildImage
import sys


print( sys.argv[0])

print( sys.argv[1])

print(len(sys.argv))
buildImage = buildImage()
parseJson = ParseBuildData()
buildImage.readJsonFile()
parseJson.parseBuild(buildImage.jsonData['devops'])
buildImage.build()