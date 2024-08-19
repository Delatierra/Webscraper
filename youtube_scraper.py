from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

import time

import pandas as pd

link= "https://www.youtube.com/@ZyoniK/videos"
driver= webdriver.Chrome()
driver.get(link)

options= webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('log-level=INT')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#COOKIES ABLEHNEN
driver.find_element(By.XPATH,"//span[contains(text(),'Reject all')]").click()

#RUNTER SCROLLEN
scroll_pause_time = 0.5  # Pause zwischen Scrolls
videos_limit = 49        # Anzahl an Videos

videos_collected = 0
while videos_collected < videos_limit:
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(scroll_pause_time)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    videos = soup.find_all("div", {"id": "details"})
    videos_collected = len(videos)

# Erste 50
videos = videos[:videos_limit]

master_list=[]

for video in videos:
    data_dict={}
    data_dict["title"]= video.find("yt-formatted-string",{"id":"video-title"}).text
    data_dict["video_url"]= "https://www.youtube.com/" + video.find("a", {"id":"video-title-link"})["href"]
    meta= video.find_all("span",{"class":"inline-metadata-item style-scope ytd-video-meta-block"})
    data_dict["views"]= meta[0].text
    data_dict["video_age"] = meta[1].text
    master_list.append(data_dict)
    
youtube_df= pd.DataFrame(master_list)

def convert_views(df):
    if "K" in df["views"]:
        views= float(df["views"].split("K")[0])*1000
        return views
    elif 'M' in df["views"]:
        views= float(df["views"].split("M")[0])*1000000 

youtube_df["CLEAN_VIEWS"]= youtube_df.apply(convert_views, axis=1)
youtube_df.to_csv("Youtube_list_zionik.csv", index=False)   

#yt-formatted-string[@id="video-title"]
#//div/h3/a/yt-formatted-string