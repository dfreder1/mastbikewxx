# Python 3
from mastodon import Mastodon
import datetime
from sys import platform as _platform
#
# Define the cities considered
#
cities = ['SAC','SF','PDX','SV']
#cities = ['SV']
#
# Open the txt file previously created and create python List of tweets by cycling through the txt file
#
if _platform == "linux" or _platform == "linux2":
   f = open('/home/dougdroplet2/projects/BikeWxX/mastbikewxx/data/forecast.txt','r')
elif _platform == "darwin":
   f = open('data/forecast.txt','r')
elif _platform == "win32":
   print('if on win32, create a dir and continue')
#
toottextlist = []
for item in f:
    toottextlist.append(item)
f.close
print(toottextlist[0])
print()
#
# Cycle through the cities, get the tokens, make the tweet, send the tweet
#
dict={}
#
#   If it is before noon, send the ridein
#   If it is after noon, send the ridehome
#   Below assumes the server is on local time
now = datetime.datetime.now()
i = 0
#   
for city in cities:
    if _platform == "linux" or _platform == "linux2":
        e = open('/home/dougdroplet2/projects/BikeWxX/bikewxxkeys/'+city+'keys','r')
    elif _platform == "darwin":
        e = open('../bikewxxkeys/'+city+'keys','r') 
    elif _platform == "win32":
        print('create dir and continue')
    dict = eval(e.read())
    access_token = dict['ACCESS_TOKEN']
    #
    if datetime.time(now.hour)<datetime.time(12,0):     
        ride='Morning ride in: '
        toottext = ride
        if toottextlist[i+1][:7] == 'No data':
            toottext = toottext
        else:
            toottext = toottext + toottextlist[i+1] +' #bike #bikecommute'
        if toottextlist[i+9][:7] == 'No data':
            toottext = toottext
        else:
            toottext = toottext + toottextlist[i+9] +' #bike #bikecommute'
        if toottextlist[i+17][:7] == 'No data':
            toottext = toottext
        else:
            toottext = toottext + toottextlist[i+17] +' #bike #bikecommute'
        if toottextlist[i+25][:7] == 'No data':
            toottext = toottext
        else:
            toottext = toottext + toottextlist[i+25] +' #bike #bikecommute'
        if toottextlist[i+2][:7] == 'No data':
            toottext = toottext
        else:    
            toottext = toottext + 'Ride home: ' + toottextlist[i+2]
    else:
        ride='Evening ride home: '
        toottext = ride
        if toottextlist[i+1][:7] == 'No data':
            toottext = toottext
        else:
            toottext = toottext + toottextlist[i+1] +' #bike #bikecommute'
        if toottextlist[i+10][:7] == 'No data':
            toottext = toottext
        else:
            toottext = toottext + toottextlist[i+10] +' #bike #bikecommute'
        if toottextlist[i+18][:7] == 'No data':
            toottext = toottext
        else:
            toottext = toottext + toottextlist[i+18] +' #bike #bikecommute'
        if toottextlist[i+26][:7] == 'No data':
            toottext = toottext
        else:
            toottext = toottext + toottextlist[i+26] +' #bike #bikecommute'
    print("")
    print(city)
    print(toottext)
    print(access_token)
    mastodon = Mastodon(
        access_token = access_token,
        api_base_url = 'https://bot.ave5.dev/'
    )
    mastodon.status_post(toottext)

#api.update_status(toottext) 
#    print('tweets away!')
    i += 2
    e.close
#
