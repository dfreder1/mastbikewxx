##Project

Source code for creating a simple twice-daily matrix and mastodon bot to report the bike commute weather for Sacramento, San Francisco, Silicon Valley, and Portland.

Currently running on mastodon bots bots: @bikewxsac, @BikeWxSF, @BikeWxPDX, and @BikeWxSV all at @bot.ave5.dev
(Previously running at twitter accounts: @bikewxsac, @BikeWxSF, @BikeWxPDX, and @BikeWxSV)

##Operation

'get_wx_data.py' grabs basic weather data from:

https://api.weather.gov/points/

http://www.airnowapi.org/

http://api.openweathermap.org/

https://tidesandcurrents.noaa.gov/api-helper/url-generator.html

and places the data into a text file.

'tweet_wx_data' composes the tweets using the twitter api.


