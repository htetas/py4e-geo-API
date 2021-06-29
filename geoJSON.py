#program to extract geo locations using JSON from py4e
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#py4e service url & api_key
api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"

while True:
    #input for address
    address = input("Enter address: ")
    #stopping the program if person enter without entering address
    if len(address)<1 : break
    #creating url for google api
    url = serviceurl + urllib.parse.urlencode({'address':address, 'key':api_key})
    #requesting json from google and storing data
    urlh = urllib.request.urlopen(url)
    data = urlh.read().decode()
    print("Retriving", url)
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('Fail to retrive data')
        continue

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    placeID = js['results'][0]['place_id']
    print(placeID)
