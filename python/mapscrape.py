import requests #Handles making requests to the server
from bs4 import BeautifulSoup #parses html and xml
import json #parses json
import time #used to generate a timestamp

#This is the common base url for both the scrapes we will be running here
base_url = "http://outagecenter.pseg.com/data/interval_generation_data/"

#generate the timestamp and turn it into a string for concatenation
timestamp = str(time.time())

#build the metadata url to get the directory for the second scrape
metadata_url = base_url + "metadata.xml?timestamp=" + timestamp

#make the request to the server
metadata_request = requests.get(metadata_url)

#load the response into an xml parser
xml = BeautifulSoup(metadata_request.text)

#get the directory we need
data_directory = xml.find('directory').text

#build the data url
data_url = base_url + data_directory + "/data.js?timestamp=" + timestamp

#make the request for the data
data_request = requests.get(data_url)

#load the response into a json parser
data_results = json.loads(data_request.text)

#grab only the portion of the results we care about

results = data_results['file_data']

print str(results['total_customers']) + " total customers"
print str(results['total_outages']) + " total outages"
print str(results['total_served']) + " total served"


