#How to Parse a Website with regex and urllib

import urllib.parse
import urllib.request
import re

url = 'https://kotaku.com/'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()
#print(respData)

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData)) #search for any characters between <p></p>
#can add other variables to receive other stuff quick example of how this can help out with

for eachP in paragraphs:
    print(eachP)