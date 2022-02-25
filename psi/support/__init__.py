import psi.support.log
def defineProperties(siteObj):
    logF = psi.support.log.logFile('psi.support.log', 'General', 'All')
    logF.log('INFO', 'Got request to create properties for '+siteObj.cleanURL)
    try:
        siteObj.score = siteObj.rdump["lighthouseResult"]["categories"]["performance"]["score"]
        logF.log('INFO', 'Define '+siteObj.cleanURL+' score as '+str(siteObj.score))
        siteObj.fetchTime = siteObj.rdump["lighthouseResult"]["fetchTime"]
        logF.log('INFO', 'Define '+siteObj.cleanURL+' fetchTime as '+str(siteObj.fetchTime))
        siteObj.id = siteObj.rdump["id"]
        logF.log('INFO', 'Define '+siteObj.cleanURL+' id as '+str(siteObj.id))
        siteObj.userAgent = siteObj.rdump["lighthouseResult"]["userAgent"]
        logF.log('INFO', 'Define '+siteObj.cleanURL+' userAgent as '+siteObj.userAgent)
        siteObj.benchmarkIndex = siteObj.rdump["lighthouseResult"]["environment"]["benchmarkIndex"]
        logF.log('INFO', 'Define '+siteObj.cleanURL+' benchmarkIndex as '+str(siteObj.benchmarkIndex))
        siteObj.networkServerLatency = siteObj.rdump["lighthouseResult"]["audits"]["network-server-latency"]["displayValue"]
        logF.log('INFO', 'Define '+siteObj.cleanURL+' networkServerLatency as '+str(siteObj.networkServerLatency))
        siteObj.serverResponseTime = siteObj.rdump["lighthouseResult"]["audits"]["server-response-time"]["details"]["items"][0]["responseTime"]
        logF.log('INFO', 'Define '+siteObj.cleanURL+' serverResponseTime as '+str(siteObj.serverResponseTime))
        siteObj.interactive = siteObj.rdump["lighthouseResult"]["audits"]["interactive"]["numericValue"]
        logF.log('INFO', 'Define '+siteObj.cleanURL+' interactive as '+str(siteObj.interactive))
        siteObj.totalBlockingTime = siteObj.rdump["lighthouseResult"]["audits"]["total-blocking-time"]["displayValue"]
        logF.log('INFO', 'Define '+siteObj.cleanURL+' totalBlockingTime as '+str(siteObj.totalBlockingTime))
        siteObj.networkRtt = siteObj.rdump["lighthouseResult"]["audits"]["network-rtt"]["displayValue"]
        logF.log('INFO', 'Define '+siteObj.cleanURL+' networkRtt as '+str(siteObj.networkRtt))
        siteObj.speedIndex = siteObj.rdump["lighthouseResult"]["audits"]["speed-index"]["displayValue"]
        logF.log('INFO', 'Define '+siteObj.cleanURL+' speedIndex as '+str(siteObj.speedIndex))
    except Exception as exp:
        logF.log('ERR', 'Exception defining properties: '+str(exp))