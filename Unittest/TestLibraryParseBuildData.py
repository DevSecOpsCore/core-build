# coding=utf-8
import unittest

from Library.Classes.parseBuildData import ParseBuildData
from Library.Classes.build import buildImage


class TestLibraryParseBuildData(unittest.TestCase):



    def test_json_devops_control(self):
        ParseBuildData.commandParameters = {
            'jPath': '../',
            'jName': 'devops-settings-example.json'
        }
        resultReadJson = buildImage.readJsonFile()

        if 'devops' in resultReadJson:
            print ('Gonderilen json data icerisinde -devops- dizini bulundu. Adim basarili sekilde tamamlanmistir.')
            test = True
            self.assertEqual(True, test)
        else:
            print ('Gonderilen json data icerisinde -devops- dizini bulunamadi !! Lutfen Json dosyasini kontrol ediniz.')
            test = False
            self.assertEqual(True, test)

    def test_json_details_control(self):
        ParseBuildData.commandParameters = {
            'jPath': '../',
            'jName': 'devops-settings-example.json'
        }
        resultReadJson = buildImage.readJsonFile()

        if 'details' in resultReadJson['devops']:
            print ('Gonderilen json data icerisinde -[devops][details]- dizini bulundu. Adim basarili sekilde tamamlanmistir.')
            test = True
            self.assertEqual(True, test)  # add assertion hereS

        else:
            print ('Gonderilen json data icerisinde -[devops][details]- dizini bulunamadi !! Lutfen Json dosyasini kontrol ediniz.')
            test = False
            self.assertEqual(True, test)  # add assertion hereS

    def test_json_build_control(self):
        ParseBuildData.commandParameters = {
            'jPath': '../',
            'jName': 'devops-settings-example.json'
        }
        resultReadJson = buildImage.readJsonFile()

        if 'build' in resultReadJson['devops']:
            print (
                'Gonderilen json data icerisinde -[devops][build]- dizini bulundu. Adim basarili sekilde tamamlanmistir.')
            test = True
            self.assertEqual(True, test)  # add assertion hereS

        else:
            print (
                'Gonderilen json data icerisinde -[devops][build]- dizini bulunamadi !! Lutfen Json dosyasini kontrol ediniz.')
            test = False
            self.assertEqual(True, test)  # add assertion hereS

    def test_parseBuildData(self):
        ParseBuildData.commandParameters = {
            'jPath': '../',
            'jName': 'devops-settings-example.json'
        }
        resultReadJson = buildImage.readJsonFile()
        ParseBuildData.parseBuild(resultReadJson['devops'])
        print('Json Data Parser a gonderildi , parser func kontrol ediliyor.' )

        if 'platform' in ParseBuildData.build[0]:
            print ("Parser Func -[devops][build] adımını basarili sekilde parse etmistir.")
            test = True
            self.assertEqual(True, test)  # add assertion hereS

        else:
            print ("Parser Func -[devops][build] alanını parse edememistir !! Lutfen Json Dosyasını kontrol ediniz.")
            test = False
            self.assertEqual(True, test)  # add assertion hereS

        if 'imageName' in ParseBuildData.details[0]:
            print ("Parser Func -[devops][details] alanını basarili sekilde parse etmistir.")
            test = True
            self.assertEqual(True, test)  # add assertion hereS

        else:
            print ("Parser Func -[devops][build] alanını parse edememistir !! Lutfen Json Dosyasını kontrol ediniz.")
            test = False
            self.assertEqual(True, test)  # add assertion hereS


if __name__ == '__main__':
    unittest.main()
