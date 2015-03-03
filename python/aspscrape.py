import requests #module to handle the http post request
from bs4 import BeautifulSoup #module for parsing html

#This is our base url where all requests to the server will be made
url = "http://disclosurereports.astrazeneca-us.com/PhysicianReport.aspx"

#And we build our payload out here using a python dictionary. The first time through we manually assign the fields we care about and their associated values
#using information we pull from the web inspector the first time we load the page.
payload = {
    '__LASTFOCUS':'',
    '__EVENTTARGET':"",
    '__EVENTARGUMENT':"",
    '__VIEWSTATE':"/wEPDwUKMTAwNTQwNzU3MA9kFgJmD2QWAgIDD2QWAgIBD2QWAgIbD2QWAmYPZBYoAgQPDxYCHgRUZXh0BScgKEphbnVhcnkgMSwgMjAxNCB0byBEZWNlbWJlciAzMSwgMjAxNClkZAIHDw8WAh8ABQ4gTWFyY2ggMiwgMjAxNWRkAgkPFgIeB09uQ2xpY2sFZ2phdmFzY3JpcHQ6cmV0dXJuIGZuT3Blbk1lbnVIZWxwUERGKCdQZGYvUGh5c2ljaWFuIERpc2Nsb3N1cmUgSGVscF9XaG8gaXMgaW5jbHVkZWQgaW4gdGhlIHJlcG9ydC5wZGYnKTtkAgsPFgIfAQVoamF2YXNjcmlwdDpyZXR1cm4gZm5PcGVuTWVudUhlbHBQREYoJ1BkZi9QaHlzaWNpYW4gRGlzY2xvc3VyZSBIZWxwX1doYXQgaXMgaW5jbHVkZWQgaW4gdGhlIHJlcG9ydC5wZGYnKTtkAg0PFgIfAQVwamF2YXNjcmlwdDpyZXR1cm4gZm5PcGVuTWVudUhlbHBQREYoJ1BkZi9Bc3RyYVplbmVjYSBQaHlzaWNpYW4gRGlzY2xvc3VyZSBSZXBvcnRfSG93IHRvIHNlYXJjaCB0aGUgcmVwb3J0LnBkZicpO2QCDw8WAh8BBVFqYXZhc2NyaXB0OnJldHVybiBmbk9wZW5NZW51SGVscFBERignUGRmL0ZBUXNQaHlzaWNpYW5EaXNjbG9zdXJlUmVwb3J0c1BERi5wZGYnKTtkAhEPDxYCHgdWaXNpYmxlaGRkAhMPDxYCHwBlZGQCFQ8WAh4JaW5uZXJodG1sZWQCFw8WAh8CaBYCZg9kFgJmD2QWAgIDDxAPFgYeDURhdGFUZXh0RmllbGQFCFJvd190ZXh0Hg5EYXRhVmFsdWVGaWVsZAUIUm93X3RleHQeC18hRGF0YUJvdW5kZxYCHghPbkNoYW5nZQUPZm5Mb2FkU3RhdHVzKCk7EBUDAjEwAjIwAjUwFQMCMTACMjACNTAUKwMDZ2dnFgECAWQCGQ8WAh8CaGQCVQ8WAh8CaGQCWw8QDxYGHwQFClJlcG9ydFllYXIfBQUCSUQfBmdkEBUECzIwMTQgQW5udWFsCzIwMTMgQW5udWFsCzIwMTIgQW5udWFsCzIwMTEgQW5udWFsFQQcMjAxNF4zMS1ERUMtMjAxNF4wMi1NQVItMjAxNRwyMDEzXjMxLURFQy0yMDEzXjIyLU9DVC0yMDE0HDIwMTJeMzEtREVDLTIwMTJeMDktT0NULTIwMTMcMjAxMV4zMS1ERUMtMjAxMV4xMS1ERUMtMjAxMhQrAwRnZ2dnZGQCXw8PZBYEHgpPbktleVByZXNzBRxyZXR1cm4gdHh0VmFsaWRhdGlvbihldmVudCk7HglPbktleURvd24FF3JldHVybiBmbktleUVudGVyKCcxJyk7ZAJjDw9kFgQfCAUccmV0dXJuIHR4dFZhbGlkYXRpb24oZXZlbnQpOx8JBRdyZXR1cm4gZm5LZXlFbnRlcignMScpO2QCZw8PZBYEHwgFHHJldHVybiB0eHRWYWxpZGF0aW9uKGV2ZW50KTsfCQUXcmV0dXJuIGZuS2V5RW50ZXIoJzEnKTtkAmsPD2QWBB8IBRxyZXR1cm4gdHh0VmFsaWRhdGlvbihldmVudCk7HwkFF3JldHVybiBmbktleUVudGVyKCcxJyk7ZAJvDxAPFgYfBAUIU1RBVEVfSUQfBQUIU1RBVEVfSUQfBmcWAh8JBRVyZXR1cm4gZm5LZXlFbnRlcigxKTsQFTUKLS1TZWxlY3QtLQJBSwJBTAJBUgJBWgJDQQJDTwJDVAJEQwJERQJGTAJHQQJISQJJQQJJRAJJTAJJTgJLUwJLWQJMQQJNQQJNRAJNRQJNSQJNTgJNTwJNUwJNVAJOQwJORAJORQJOSAJOSgJOTQJOVgJOWQJPSAJPSwJPUgJQQQJQUgJSSQJTQwJTRAJUTgJUWAJVVAJWQQJWVAJXQQJXSQJXVgJXWRU1AAJBSwJBTAJBUgJBWgJDQQJDTwJDVAJEQwJERQJGTAJHQQJISQJJQQJJRAJJTAJJTgJLUwJLWQJMQQJNQQJNRAJNRQJNSQJNTgJNTwJNUwJNVAJOQwJORAJORQJOSAJOSgJOTQJOVgJOWQJPSAJPSwJPUgJQQQJQUgJSSQJTQwJTRAJUTgJUWAJVVAJWQQJWVAJXQQJXSQJXVgJXWRQrAzVnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAnMPD2QWBB8IBRxyZXR1cm4gdHh0VmFsaWRhdGlvbihldmVudCk7HwkFF3JldHVybiBmbktleUVudGVyKCcxJyk7ZAJ3Dw9kFgQfCAUccmV0dXJuIHR4dFZhbGlkYXRpb24oZXZlbnQpOx8JBRdyZXR1cm4gZm5LZXlFbnRlcignMScpO2Rk5dkB9SkHWs1EVbtOezHZGT7tTqY=",
    '__VIEWSTATEGENERATOR':'4BF882FA',
    'ctl00$ContentPlaceHolder1$hdnStartIndex':0,
    'ctl00$ContentPlaceHolder1$hdnEndIndex':0,
    'ctl00$ContentPlaceHolder1$hdnPhysicianPerPageCount':1,
    'ctl00$ContentPlaceHolder1$hdnPreviousPhysicianCount':1,
    'ctl00$ContentPlaceHolder1$hdnPrevoiosStartIndex':1,
    'ctl00$ContentPlaceHolder1$hdnButtonValue':'NEXT',
    'ctl00$ContentPlaceHolder1$hdnTotalPage':1,
    'ctl00$ContentPlaceHolder1$hdnJumpName':'',
    'ctl00$ContentPlaceHolder1$hdnCurrentIndex':1,
    'ctl00$ContentPlaceHolder1$hdncurrentcount':10,
    'ctl00$ContentPlaceHolder1$hdnPageCount':'',
    'ctl00$ContentPlaceHolder1$hdnSearchValue':'',
    'ctl00$ContentPlaceHolder1$ddlTimePeriod':'2014^31-DEC-2014^02-MAR-2015',
    'ctl00$ContentPlaceHolder1$txtFirstName':'',
    'ctl00$ContentPlaceHolder1$txtMIName':'',
    'ctl00$ContentPlaceHolder1$txtLastName':'',
    'ctl00$ContentPlaceHolder1$txtCity':'',
    'ctl00$ContentPlaceHolder1$ddlState':'',
    'ctl00$ContentPlaceHolder1$txtZipCode':'',
    'ctl00$ContentPlaceHolder1$txtEntity':'',
    'ctl00$ContentPlaceHolder1$btnResetSearch':''
    }

#There are a lot of pages we could scrape, but this example only scrapes the first four pages using the range() function
for index in range(4):
    #make the reqest to the webserver
    response = requests.post(url, data = payload)


    #load it into an html parser
    html = BeautifulSoup(response.text)

    #Isolate the table we care about by first targeting the container div, then the table

    container = html.find('div',{'id':'ctl00_ContentPlaceHolder1_pnlReports'})

    table = container.find('table')

    #from that table, grab the rows

    rows = table.find_all('tr')

    for row in rows:
        #There is a lot of work that could be done to clean up this table. However we are focusing only on the actual scrape, so we will only print out the first cell which should have a name in it. There are blank cells in the first column because each payment entry spans multiple rows.
        cells = row.find_all('td')
        #normally here is where you would write out to a csv or import into a database after cleaning the rows.
        print cells[0].text

    #Now we are going to go through and repopulate all the values for the payload we need. Since we are looping, the original payload variable will be overwritten with the new payload.
    #We start by selecting the existing form fields and their values on the html page we just scraped
    form = html.find_all('input',{'type':'hidden'})
    #We declare an empty payload variable to wipe out the existing payload
    payload = {}

    #now we loop through all the fields
    for field in form:
        #since not all fields have values, we need to write in some error handling for those cases where there is no associated value with the field
        try:
            #So these fields have corresponding values and we assign them to the appropriate field
            payload[field['name']] = field['value']
        except KeyError:
            #These fields do not have values, so we assign an empty string to those fields
            payload[field['name']] = ""
    #Now here is where incrementing comes into play, on the first iteration we assign the value of one to the index
    if index == 0:
        increment = 1

    else:
        #subsequent iterations increment that value by 20 - the number of payment records on each page.
        increment += 20

    #And now we concatenate that increment with a control that is assigned to the __EVENTTARGET field - the function that tells the server what to do next.
    #Essentially we are telling the server to return the next 20 results. The key to figuring this out is manually navigating through the first few pages of
    #the web app we are scraping and checking to see how the fields change as they are passed in the header information to the server 
    payload['__EVENTTARGET'] = "ctl00$ContentPlaceHolder1$pnlBottom" + str(increment + 20)

