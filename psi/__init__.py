import requests
import json
import psi.support
apikey = None
class newSite:
    def __init__(self, url) -> None:
        if url.startswith("http://") == True:
            self.url = url
            self.cleanURL = url.strip('http://')
        elif url.startswith("https://") == True:
            self.url = url
            self.cleanURL = url.strip('https://')
        elif url.startswith("www") == True:
            self.url = "http://" + url
        else:
            self.url = "http://" + url
    def getResult(self):
        if apikey == None:
            raise Exception("Unable to create site object, no API key defined.")
        requestUrl = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?key=' + apikey + '&url=' + self.url
        r = requests.get(requestUrl)
        if r.status_code != 200:
            raise Exception("Unable to query, API returned code " + str(r.status_code))
        else:
            self.score = r.json()["lighthouseResult"]["categories"]["performance"]["score"]
            self.rdump = r.json()
            self = psi.support.defineProperties(self)
    def saveResult(self, filename):
        with open(filename, 'w') as saveFile:
            saveFile.write(json.dumps(self.rdump))
    def readResult(self, filename):
        with open(filename, 'r') as saveFile:
            self.rdump = json.loads(saveFile.read())
            self.score = self.rdump["lighthouseResult"]["categories"]["performance"]["score"]
            self = psi.support.defineProperties(self)
