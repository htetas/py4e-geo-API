#program to extract geo location using xml from py4e
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#py4e geo serviceurl & api_key
api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/xml?"

while True:
    #asking for address input
    address = input("Enter Address: ")
    #shutting the program if user press Enter
    if len(address) < 1: break
    #getting url to request xml
    url = serviceurl + urllib.parse.urlencode({'address': address, 'key': api_key})
    #requesting xml
    xml = urllib.request.urlopen(url, context = ctx).read().decode()
    print('Retrieving data from', url)
    #using ElementTree function
    try:
        data = ET.fromstring(xml)
    except:
        data = None
    if not data or data.find('status').text != 'OK':
        print('Fail to retrive data')

    results = data.findall('result')
    print('Printing Results', results)
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    print('lat', lat, 'lng', lng)
    location = results[0].find('formatted_address').text
    print(location)
    placeID = results[0].find('place_id').text
    print(placeID)
