import requests
import json
apikey = None
class newSite:
    def __init__(self, url) -> None:
        self.cleanURL = url.strip('http://')
        self.cleanURL = self.cleanURL.strip('https://')
        if url.startswith("http") == True:
            self.url = url
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
    def getTestProperty(self, property):
        match property:
            case "id":
                return(self.rdump["id"])
            case "userAgent":
                return(self.rdump["lighthouseResult"]["userAgent"])
            case "fetchTime":
                return(self.rdump["lighthouseResult"]["fetchTime"])
            case "benchmarkIndex":
                return(self.rdump["lighthouseResult"]["environment"]["benchmarkIndex"])
            case "network-server-latency":
                return(self.rdump["lighthouseResult"]["audits"]["network-server-latency"]["displayValue"])
            case "server-response-time":
                return(self.rdump["lighthouseResult"]["audits"]["server-response-time"]["details"]["items"][0]["responseTime"])
            case "interactive":
                return(self.rdump["lighthouseResult"]["audits"]["interactive"]["numericValue"])
            case "total-blocking-time":
                return(self.rdump["lighthouseResult"]["audits"]["total-blocking-time"]["displayValue"])
            case "network-rtt":
                return(self.rdump["lighthouseResult"]["audits"]["network-rtt"]["displayValue"])
            case "speed-index":
                return(self.rdump["lighthouseResult"]["audits"]["speed-index"]["displayValue"])
            case "dump":
                return(self.rdump)
    def saveResult(self, filename):
        with open(filename, 'w') as saveFile:
            saveFile.write(json.dumps(self.getTestProperty('dump')))
    def readResult(self, filename):
        with open(filename, 'r') as saveFile:
            self.rdump = json.loads(saveFile.read())
            self.score = self.rdump["lighthouseResult"]["categories"]["performance"]["score"]
