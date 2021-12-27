from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

youtube_trending_url = "https://www.youtube.com/feed/trending"

# creating a function so we don't have to run the function out again and again

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    return driver 

def get_videos(driver):
    video_div_tag = "ytd-video-renderer"
    driver.get(youtube_trending_url)
    videos = driver.find_elements(By.TAG_NAME, video_div_tag)
    return videos

#this function will return a dictionary
def parse_videos(video):
    title_tag = video.find_element(By.ID, 'video-title')
    title = title_tag.text
    # getting url of video
    url = title_tag.get_attribute('href')
    
    # getting thumbnail of url, first get thumbnail tag and then url 
    thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
    thumbnail_url = thumbnail_tag.get_attribute('src')

    # finding channel
    channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
    channel_name = channel_div.text

    #showing number of views
    num_tag = video.find_element(By.ID, "metadata-line")
    # this returns a list because we are looking for elements not element
    num_views = num_tag.find_elements(By.TAG_NAME, 'span')
    # to see text you have to put .text
    num_views_total = num_views[0].text.replace(" views", "")
    #num_views_total = num_views
    hours_uploaded = num_views[1].text

    #showing description of video
    description = video.find_element(By.ID, 'description-text').text

    return{
        'title':title,
        'url':url,
        'thumbnail_url':thumbnail_url,
        'channel_name':channel_name,
        'num_views_total':num_views_total,
        'hours_uploaded':hours_uploaded,
        'description':description
    }

if __name__ == "__main__":
    print('Creating driver')
    driver = get_driver()

    print('Fetching trending videos')
    videos = get_videos(driver)
    

    #print('Get the videos')
    #video_div_tag = "ytd-video-renderer"
    
    #print('Page Title:', driver.title)  
    print(f'Found {len(videos)} videos')
    print('Parsing top 10 videos')
    # list comprehension
    video_data = [parse_videos(video) for video in videos[:11]]
    print(video_data)

    print('Saving the data to CSV')
    videos_df = pd.DataFrame(video_data)
    print(videos_df)
    # to avoid having an index column, add index=None
    # make sure to store as .csv file
    videos_df.to_csv('trending.csv', index=None)
    # infor to extract, title, url, thumbnail_url, channel, views, uploaded, description
    # selecting 1st video
    #video = videos[0]
    # getting title of video
    
    # xpath in selenium, used it for span
    
    
    
    #print('Title: ', title)
    #print('URL: ', url)
    #print('Thumbnail URL: ', thumbnail_url)
    #print('Channel name: ', channel_name)
    #print('Num views: ', num_views_total)
    #print('Uploaded time: ', hours_uploaded)
    #print('Description: ', description)
    #print(type(num_views))
    #print(type(num_tag))



# need to create webdriver


