
# Github Composite Action -  Build From Python 


Bu proje python kullanılarak container image build etme işlemini yapmaktadır. 
Github action workflow'larınızdan parametreleri vererek workflow'unuzda çağırabilir ve image build işlemini yaptırabilirsiniz.


# Çalışma prensibi : 
![Logo](https://user-images.githubusercontent.com/38957716/154684078-d8350610-6c86-4872-bf86-83784a91122b.png)

Build edilecek olan uygulamanın içerisine koyulacak olan json dosyası image 'ın hangi özelliklerde 
olacağını belirtmektedir. Aşağıda örnek json yapısını görmektesiniz. 

```json
   {
    "devops":
    {
        "build": [
            {
                "builder": "podman"
            },
            {
                "builder": "buildah"
            }
          ],
        "details":
            {
                "responsible": "A team",
                "domain": "coreBanking",
                "app": "swo-core",
                "imageName":"image-test",
                "registryName":"docker.io",
                "dockerFilePath":"",
                "tag":"enes1",
                "dockerFileName":"Dockerfile_example",
                "repositoryName":"enespekdas"
            }
          ,
        
      

    }

  }
```

Yukarıdaki Json dosyasını inceleyelim ve hangi adım ne anlama geliyor detaylandıralım:

```json

{
  "devops":{

  }
}
```
İster build adımı için özel bir json oluşturun , isterseniz de kodunuzun içerisinde mevcut olan bir json dosyasının içine entegre edin farketmeksizin çalışacak şekilde ayarlanmıştır.
Dikkat eidlmesi gereken noktalar , ana dallanmada " { } " ( süslü parantez içi kastedilmektedir) "devops" başlığı altına yazılmalıdır.


```json

{
  "devops":{
      "build":{

      },
      "details":{

      }
  }
}
```
Build product'ı "build" ve "details" alanlarından beslenerek işlem yapmaktadır. 
"build" içerisinde hangi builder ile build işlemi yapılacağı belirtilmektedir. 
"details" alanında ise build olacak imaja ait özellikler verilmektedir. 

```json
 "details":
            {
                "imageName":"image-test",
                "dockerFilePath":"",
                "tag":"enes1",
                "dockerFileName":"Dockerfile_example",
            }
          ,
```

"imageName" --> Alanı Dockerfile'dan oluşturulacak olan image'ın ismini belirtmektedir.

"tag" --> Alanı , image'in hangi tag ile oluşturulacağını belirtmektedir "v1 , v2 , v1.1" gibi.

"dockerFileName" --> Image'ın oluşturulacağı dockerfile'ın adını belirtmektedir. Default olarak "Dockerfile" olarak verilmektedir.

"dockerFilePath" --> Dockerfile'ın bulunduğu path'i belirtmektedir. Default olarak kodların bulunduğu ana dizini almaktadır.



