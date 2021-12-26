from selenium import webdriver
from selenium.webdriver.chrome.options import Options

youtube_trending_url = "https://www.youtube.com/feed/trending"

# creating a function so we don't have to run the function out again and again

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    return driver 

if __name__ == "__main__":
    driver.get(youtube_trending_url)

    print('Page Title:', driver.title)  





# need to create webdriver


