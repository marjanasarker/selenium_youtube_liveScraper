# moving items from scraper.py that will not be used
import requests
from bs4 import BeautifulSoup

youtube_trending_url = "https://www.youtube.com/feed/trending"

# requests to get data from library
# requests do not execute javascript
# need to create a headless browser - selenium - will automate refreshing and browsing
# using selenium to create a browser driver 
# downloading chrome driver to use with selenium 
# replit comes with chromedriver, you can check version with chromedriver --v
# making a response object 
response = requests.get(youtube_trending_url)




# if status code is 200, this means successfully managed to get information
print('Status Code', response.status_code)
# output of response
# print('Output', response.text)
# output of response - first thousand characters
# print('Output', response.text[:1000])
# save response to HTML 
#with open('trending.html', 'w') as f:
    #f.write(response.text)

#creating beautiful soup object to find items from html page
doc = BeautifulSoup(response.text, 'html.parser')

print('Page Title:', doc.title.text)
# find all the video divs
video_divs = doc.find_all('div', class_= 'ytd-video-renderer')
# using f string to use python variable in string so output will still be in string but operation with python variable 
print(f"Found {len(video_divs)} videos")