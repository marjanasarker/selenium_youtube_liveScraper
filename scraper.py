from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import smtplib
import os
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
def send_email():
    #gmail_user="senderemail.tester86@gmail.com"
    #print('Password', gmail_password)
    try:
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()
        sender_email = "senderemail.tester86@gmail.com"
        receiver_email = "senderemail.tester86@gmail.com"
        gmail_password=os.environ['gmail_password']
        #sent_from = sender_email
        #to = [receiver_email]
        subject = 'Test Message'
        body = 'Hey, this is a test from replit'

        email_text = f"""\
        From: {sender_email}
        To: {receiver_email}
        Subject: {subject}

        {body}
        """ 
        server_ssl.login(sender_email, gmail_password)
        server_ssl.sendmail(sender_email, receiver_email, email_text)
        server_ssl.close()
        #starttls makes sure communication is secure or you can use ssl
        #server.starttls()
    except:
        print('Bad Connection')

if __name__ == "__main__":
    #print('Creating driver')
    #driver = get_driver()

    #print('Fetching trending videos')
    #videos = get_videos(driver)
    

    #print('Get the videos')
    #video_div_tag = "ytd-video-renderer"
    
    #print('Page Title:', driver.title)  
    #print(f'Found {len(videos)} videos')
    #print('Parsing top 10 videos')
    # list comprehension
    #video_data = [parse_videos(video) for video in videos[:11]]
    #print(video_data)

    #print('Saving the data to CSV')
    #videos_df = pd.DataFrame(video_data)
    #print(videos_df)
    # to avoid having an index column, add index=None
    # make sure to store as .csv file
    # index=None takes out the index in csv file
    #videos_df.to_csv('trending.csv', index=None)
    # infor to extract, title, url, thumbnail_url, channel, views, uploaded, description
    # selecting 1st video
    #video = videos[0]
    # getting title of video
    
    # xpath in selenium, used it for span
    
    
    print("send an email with results")
    #creating send email function
    send_email()


