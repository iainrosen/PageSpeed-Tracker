import requests
with open('requests.txt', 'r') as reqFile:
    for line in reqFile:
        strippedLine = line.rstrip()
        print('Making request for: ' + strippedLine)
        requestUrl = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?key=AIzaSyB5DJDrXQlR9zgt2XYZdFEbIw3XoyjgBqA&url=' + strippedLine
        r = requests.get(requestUrl)
        print("Request completed, got code: " + str(r.status_code))
        if r.status_code == 200:
            print("Saving to file")
            with open('dump.txt', 'w') as outFile:
                outFile.write(r.text)
            resultJson = r.json()
            print("Result: " + str(resultJson["lighthouseResult"]["categories"]["performance"]["score"]))
        else:
            print("Unable to pull results, is quota exceeded?")