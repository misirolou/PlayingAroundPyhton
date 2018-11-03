#Three main modules to be used os - operating system, time, sys -system
import os
import time
import sys

cur = os.getcwd() #trying to get the path that we are in
print(cur)
'''
creating, renaming and removing files
os.mkdir("newDir") # creates new directory

time.sleep(2)  #pauses for 2 secs
os.rename("newDir", "newDir21") #renames a directory
time.sleep(2)
os.rmdir("newDir21") #removes the directory
'''

sys.stderr.write('test\n') #error text
sys.stderr.flush()
sys.stdout.write("This is stdout text\n")

#sys.argv displays all arguments even from other languages
print(sys.argv) 
if len(sys.argv) > 1:
    print(sys.argv[1]) #reference to the argument in position 1

#you can create a function argument to receive arguments from other languages
def main(arg):
    print(arg)

main(sys.argv)

import urllib.request
import urllib.parse
#getting data from the net
#x = urllib.request.urlopen('https://www.google.com/')
#print(x.read()) #receives all information from site, html,css,etc
'''
a bunch of ways to play around with sites
url = 'http://pythonprogramming.net'
values = {'s':'basic',
          'submit':'search'} #simple values to set a search for the word basic

data = urllib.parse.urlencode(values) #parse the url
data = data.encode('utf-8')
req = urllib.request.Request(url, data) #request the url services
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)
'''
#should give an error message here as google doesn´t allow to add code to site
try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())
except Exception as e:
    print(str(e))

#way of getting around issue presented above
try: 
    url = 'https://www.google.com'
    urlsearch = '/search?q=test'
    urladd = url + urlsearch

    headers = {}
    headers['User-Agent'] = 'My User Agent 1.0 From : youremail@domain.com'
    req = urllib.request.Request(urladd, headers=headers) #changing default headers to new headers way of getting around errors
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('Modules/withHeaders.txt', 'w') #created file to save info
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    print(str(e))