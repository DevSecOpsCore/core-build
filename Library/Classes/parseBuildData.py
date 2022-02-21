import argparse
from ast import arg


class ParseBuildData:
    build = []
    helm = []
    details = []
    securityTest = []
    commandParameters = {}

    def __init__(self):
        pass

    @staticmethod
    def parseBuild(value):
        class_parse_json_data = ParseBuildData()
        if type(value) == type(dict()):
            class_parse_json_data.ArrayCreation(value)
        elif type(value) == type(list()):
            for val in value:
                if type(val) == type(str()):
                    pass
                elif type(val) == type(list()):
                    pass
                else:
                    class_parse_json_data.ArrayCreation(val)
        return value

    def ArrayCreation(self, data):
        class_parse_json_data = ParseBuildData()

        for key, value in data.items():
            if str(key) == 'build':
                self.build.append(class_parse_json_data.parseBuild(value))
            elif str(key) == 'details':
                self.details.append(class_parse_json_data.parseBuild(value))
            elif str(key) == 'SecurityTest':
                self.securityTest.append(class_parse_json_data.parseBuild(value))
            elif str(key) == 'helm':
                self.helm.append(class_parse_json_data.parseBuild(value))

    @staticmethod
    def splitSysParams():
        parser = argparse.ArgumentParser()
        parser.add_argument("-jp", "--jPath", required=False)
        parser.add_argument("-jn", "--jName", required=False)
        args = parser.parse_args()
        if args.jName is None:
            ParseBuildData.commandParameters['jName'] = 'devops-settings-example.json'
        else:
            if 'json' in args.jName:
               ParseBuildData.commandParameters['jName'] = args.jName
            else:
                ParseBuildData.commandParameters['jName'] = args.jName+'.json'
        if args.jPath is None:
            ParseBuildData.commandParameters['jPath'] = ''
        elif args.jPath == 'default':
            ParseBuildData.commandParameters['jPath'] = ''
        else:
            ParseBuildData.commandParameters['jPath'] = args.jPath