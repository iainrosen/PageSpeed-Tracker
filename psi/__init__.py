import requests
import json
import psi.support
import psi.support.log
log = psi.support.log.logFile('psi.log', 'General', 'All')
log.log('INFO', 'PSI Initializing.')
#DO INIT
apikey = None
#FINISH INIT
log.log('INFO', 'PSI init completed.')
class newSite:
    def __init__(self, url) -> None:
        log.log('INFO', 'New class object created: '+url)
        if url.startswith("http://") == True:
            self.cleanURL = url.strip('http://')
            self.url = url
            log.log('INFO', 'OPT1 Clean URL defined as: '+self.cleanURL)
        elif url.startswith("https://") == True:
            self.cleanURL = url.strip('https://')
            self.url = url
            log.log('INFO', 'OPT2 Clean URL defined as: '+self.cleanURL)
        elif url.startswith("www") == True:
            self.cleanURL = url
            self.url = "http://" + url
            log.log('INFO', 'OPT3 Clean URL defined as: '+self.cleanURL)
        else:
            self.cleanURL = url
            self.url = "http://" + url
            log.log('INFO', 'OPT4 Clean URL defined as: '+self.cleanURL)
        log.log('INFO', 'Object init completed: '+url)
    def getResult(self):
        log.log('INFO', 'Got call to pull info for: '+self.url)
        if apikey == None:
            log.log('CRIT', 'API key not defined, unable to request.')
            raise Exception("Unable to create site object, no API key defined.")
        requestUrl = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?key=' + apikey + '&url=' + self.url
        log.log('INFO', 'Requesting: '+requestUrl)
        r = requests.get(requestUrl)
        if r.status_code != 200:
            log.log('CRIT', 'Got bad request status code: '+str(r.status_code))
            raise Exception("Unable to query, API returned code " + str(r.status_code))
        else:
            log.log('INFO', 'Got request status code: '+str(r.status_code))
            log.log('INFO', 'Dumping data to self.rdump from request')
            try:
                self.rdump = r.json()
                log.log('INFO', 'Completed dump.')
            except Exception as exp:
                log.log('ERR', 'Unable to dump data, got exception: '+exp)
            log.log('INFO', 'Sending to support package to define request properties')
            try:
                self = psi.support.defineProperties(self)
                log.log('INFO', 'Completed property definition')
            except Exception as exp:
                log.log('ERR', 'Unable to define, got exception: '+exp)
    def saveResult(self, filename):
        log.log('INFO', 'Got call to save results')
        try:
            log.log('INFO', 'Writing file: '+filename)
            with open(filename, 'w') as saveFile:
                saveFile.write(json.dumps(self.rdump))
            log.log('INFO', 'Completed file write to: '+filename)
        except Exception as exp:
            log.log('ERR', 'Got exception saving results: '+exp)
    def readResult(self, filename):
        log.log('INFO', 'Got call to read results')
        try:
            with open(filename, 'r') as saveFile:
                log.log('INFO', 'Reading from file: '+filename)
                self.rdump = json.loads(saveFile.read())
                self = psi.support.defineProperties(self)
        except Exception as exp:
            log.log('ERR', 'Got exception reading results: '+exp)

