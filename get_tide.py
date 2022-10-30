# Python 3
#  Testing adding tide data to San Francisco 
#
import requests, json, datetime, socket,time
from sys import platform as _platform
#
timeout = 2800
socket.setdefaulttimeout(timeout)
#
# Define the cities considered
#
cities = ['Sacramento,CA','San Francisco,CA','Portland,OR','San Jose,CA']
#
# Define additional data needed for APIs to work
#
ymd = datetime.datetime.now()
#
# Define the 'base' of the three api requests used, will later add on to these strings
#
url_tide = 'https://tidesandcurrents.noaa.gov/api/datagetter?date=today&station=9414290&product=predictions&datum=NAVD&time_zone=gmt&interval=hilo&units=english&application=bikewxx&format=json'
#
# Functions to call individual APIs
#
#
# Function for tide data from NOAA
#
def get_tide(baseurl, city):
  "This function calls the tide data from NOAA using the CO-OPS API"
  # Warning, kluge ahead!
  # This script assembles lines of text to be tweeted. Each line (now 4 lines) comes from each API call.
  # The tide api call and it's corresponding line of text only apply to San Francisco
  # So the kluge is to only run the api call only on 'Frisco. The fourth line will always be a blank for other cities,
  # but will be either the tide warning or a blank for 'Frisco.
  if city == 'San Francisco,CA':
    url = baseurl
    r = requests.get(url)
    status = r.status_code
    print(status)
    if status != 200:
      time.sleep(300)
      r = requests.get(url)
      status = r.status_code
      print(status,1)
    if status != 200:
      time.sleep(300)
      r = requests.get(url)
      status = r.status_code
      print(status,2)
    if status != 200:
      print(status,3)
      print('No data after 3 tries') 
    try:
      json_data = r.json()
      print (json_data['predictions'])
      tidev =  max(float(json_data['predictions'][0]['v']),float(json_data['predictions'][1]['v']),float(json_data['predictions'][2]['v']),float(json_data['predictions'][3]['v']))
      if tidev > 6.40:
          tidein = "Warning - Today's high tide of " + str(tidev)[:4] + ' could cause bikepath flooding in low-lying areas, see https://tidesandcurrents.noaa.gov/map/index.shtml?id=9414290 for more info'
          tidehome = tidein
      else:
          tidein = ''
          tidehome = tidein
    except:
      print(status)
      tidein = 'Tide check broken'
      tidehome = tidein
  #  f.write(tidein+'\n')
  #  f.write(tidehome+'\n')
  else:
    tidein = ''
    tidehome = tidein
  #
  f.write(tidein+'\n')
  f.write(tidehome+'\n')
  return
#
# Open a txt file and write data to it sequentially, line by line, to be assembled into a tweet in another script
#
if _platform == "linux" or _platform == "linux2":
  f = open('/home/dougdroplet2/projects/BikeWxX/BikeWxX/data/tide.txt','w')
  f.write(ymd.strftime("%c")+'\n')
elif _platform == "darwin":
  f = open('data/tide.txt','w')
  f.write(ymd.strftime("%c")+'\n')
elif _platform == "win32":
  print('if on win32, create a dir and continue')
#
# Call the APIs
#
#
# Tide from NOAA - this is just for 'frisco
#
for city in cities:
  print()
#  print(url_tide,city)
  get_tide(url_tide,city)
print()
#
#
f.close()
