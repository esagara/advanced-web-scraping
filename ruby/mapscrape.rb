require 'restclient' #This library handles reqests to the web server
require 'nokogiri' #We use this library for parsing HTML/XML
require 'json' #Library for parsing json
require 'time' #Time library for generating a timestamp

#This is the common base url used in both the scrapes we will carry out
base_url = "http://outagecenter.pseg.com/data/interval_generation_data/"

timestamp = Time.now.to_i #Generates timestamp and turns it into an integer

#build the url to get the metadata we need to scrape
metadata_url = base_url + "metadata.xml?timestamp=" + timestamp.to_s #converting timestamp to a string for concatenation

#make the web request to the server
meta_request = RestClient.get(metadata_url)

#load the response into an XML parser
xml = Nokogiri::XML(meta_request.to_s)

#get the directory tag. We do this by searching for the directory tag, specifying the first result we find and getting the content of that tag

data_directory = xml.xpath("//directory")[0].content

#build the data_url

data_url = base_url + data_directory + "/data.js?timestamp=" + timestamp.to_s

#make the webrequest

data_request = RestClient.get(data_url)

#load the data into a JSON parser which returns it as a ruby hash
data_results = JSON.parse(data_request.to_s)

#grab only the portion of the results we care about

results = data_results['file_data']

puts results['total_customers'].to_s + " total customers"
puts results['total_outages'].to_s + " total outages"
puts results['total_served'].to_s + " total served"

