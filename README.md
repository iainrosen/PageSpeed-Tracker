# PageSpeed-Tracker
 Tracks your site's PageSpeed analytics
# Basic How-To
- Create a site object with **s = psi.newSite(url)**
- Define your PageSpeed Insights API Key with **psi.apikey = 'yourapikeyhere'** (you can get your API key here: https://developers.google.com/speed/docs/insights/v5/get-started
- Get PageSpeed results with **s.getResult()**
- Save the results with **s.saveResult(filename)**
- Read results from file with **s.readResult(filename)**
- Get specific test properties with **s.getTestProperty(property)**
