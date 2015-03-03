require 'mechanize' #mechanize is a library that emulates a browser
require 'nokogiri' #nokogiri is used to parse html

#we assign a variable for the url we will query
url = 'http://disclosurereports.astrazeneca-us.com/PhysicianReport.aspx'
#and create a new browser agent using mechanize
browser = Mechanize.new()

#we do the intial query of the url
page = browser.get(url)

#and assign a numerical value to the event_target variable
increment = 1
#There are more than 11,000 pages in this web database, we will only scrape the first four here
(0..3).each do |index|
  #first we get the aspnetForm on the page and its corresponding values
  form = page.form("aspnetForm")

  #Then we overwrite the __EVENTTARGET field of the form which tells the web server
  #what to do with our request - in this case going to a specific page in the database.
  #We concatenate an index number onto the end of the function we want to assign
  #to the __EVENTTARGET field - a 1 for the first time through. The key to figur
  #out how this works is manually paging through the first few pages of a website
  #and seeing how the form values change in the web inspector as you move from one page to another.
  form.add_field!('__EVENTTARGET','ctl00$ContentPlaceHolder1$pnlBottom' + increment.to_s)
  #we also have to designate the time period we want to search for, again we get that from the web inspector
  form.add_field!('ctl00$ContentPlaceHolder1$ddlTimePeriod','2014^31-DEC-2014^02-MAR-2015')
  #We submit the form with the new __EVENTTARGET and time period variables
  page = browser.submit(form)
  #Load the response into an HTML parser
  html = Nokogiri::HTML(page.body)
  #Then isolate the table containing the data we want using css selectors made available through Nokogiri
  table = html.css('div#ctl00_ContentPlaceHolder1_pnlReports table')
  #From there we isolate the rows
  rows = table.css('tr')
  #And loop through the rows to isolate the individual table cells
  rows.each do |row|
    cells = row.css('td')
    #this table is fairly dirty and needs some work to get it into a viable data format
  #However since we are more concerned about how the scrape works, we will skip it and instead print out the first field - which typically contains a name
  #In many cases, the name field will be blank because records span multiple rows
    puts cells[0].text
  end
  #Finally we increment by the number of results per page for the next request
  increment += 20
end
