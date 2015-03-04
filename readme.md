Using the web inspector for complex scrapes
===========================================

This repo contains example scripts of scrapes in both Ruby and Python using concepts taught in the NICAR 2015 advanced web scraping course. The class focuses on using the web inspector to find the information needed to conduct more sophisticated scrapes. The slide deck for the presentation can be found [here](https://docs.google.com/presentation/d/1QU5eBUWfEXIi8CmrIXaBCVx2FOAfelbUKAZmlYKhP5Y/edit?usp=sharing).

Requirements
------------

###Python
The Python scrapes require only two modules not included with Python standard library. [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/) is a module for parsing markdown languages such as HTML and XML. [Requests](http://docs.python-requests.org/en/latest/) is used to make both get and post web requests.
Both can be installed individually using ```pip``` or together using ```pip install -r requirements.txt```. 

###Ruby
The Ruby scripts require three different libraries. The first is [Nokogiri](http://www.nokogiri.org/), Ruby's parser for HTML and XML. The ASP.NET scrape requires [Mechanize](http://www.rubydoc.info/gems/mechanize/Mechanize) to emulate a browser. [Rest-Client](http://www.rubydoc.info/gems/rest-client/1.7.3) is needed to make web requests in the mapscrape.rb example.
If you have [Bundler](http://bundler.io/) installed you can simply navigated to the Ruby directory and use ```bundle install``` to install the required libraries. Otherwise, use ```gem install <package name>```.