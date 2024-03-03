from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pytube import YouTube
import os
import csv
from urllib.parse import urlparse, parse_qs
import re

def find_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    emails = re.findall(email_pattern, text)
    return emails

def get_search_query_from_url(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    if 'search_query' in query_params:
        search_query = query_params['search_query'][0]
        return search_query
    return None
def get_social_media_link(redirect_url):
        

            parsed_url = urlparse(redirect_url)
            query_params = parse_qs(parsed_url.query)

            social_media_link = query_params.get('q', [None])[0]

            if social_media_link:
                print("Extracted  URL:", social_media_link)

            else:
                print("Facebook URL not found in the redirect URL.")  
            return social_media_link      






def scroll_page_slowly(driver):
    # Create an ActionChains object
    actions = ActionChains(driver)

    # Get the initial page height
    initial_page_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")

    # Scroll down the page until the bottom is reached
    while True:
        # Scroll down by the scroll_step
        actions.send_keys(Keys.SPACE).perform()
        time.sleep(5)  # Adjust the time delay as per your requirement

        # Get the updated page height after scrolling
        updated_page_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")

        # Check if the page height remains the same after scrolling (reached the bottom)
        if updated_page_height == initial_page_height:
            try:
                    find=driver.find_element(By.CSS_SELECTOR,"#message")
                    print("##message element found!")
                    break
            except:

                    actions.send_keys(Keys.PAGE_UP).perform()
                    actions.send_keys(Keys.SPACE).perform()
                    actions.send_keys(Keys.SPACE).perform()

        # Update the initial_page_height for the next iteration
        initial_page_height = updated_page_height

    # Scroll to the very bottom of the page
    actions.send_keys(Keys.END).perform()            


driver = webdriver.Chrome() # You can use any other browser driver as per your preference
driver.get("https://www.youtube.com/")  # Replace with your desired URL
time.sleep(2)
t=input('Enter to start..')#Press Enter after choose filerers and apply filters manually
new_search_url=driver.current_url
driver.quit()
driver = webdriver.Chrome() # You can use any other browser driver as per your preference
driver.get(new_search_url)  # Replace with your desired URL
time.sleep(5)
search_query = get_search_query_from_url(new_search_url)
search_query_formatted=search_query.strip(' ')

scroll_page_slowly(driver)
print('scroll finished')
time.sleep(2)

folder_name = "output"
if not os.path.exists(folder_name):
                    # Create the folder
                    os.makedirs(folder_name)
                    print("output Folder created successfully!")
else:
            print("output Folder already exists!")
data = set()  
current_unix_time = int(time.time())
file= open(f'output/{search_query_formatted}_{current_unix_time}.csv', 'w', encoding='utf-8', newline='')  
writer = csv.writer(file)
headers = ["Channel ID","Channel name", "Channel url", "View Count","Subscriber Count","Video Count","Email has?","Email in description?","Social media"]
writer.writerow(headers)
search_driver_options=Options()
search_driver_options.add_argument('--headless=new')
search_driver=webdriver.Chrome(options=search_driver_options) # You can use any other browser driver as per your preference 
print('Scrapig started...wait....')         
for i in driver.find_elements(By.CSS_SELECTOR,'#contents ytd-video-renderer'):
                    try:
                        
                        
                    
                    
                        
                        video_link=i.find_element(By.CSS_SELECTOR,'#thumbnail').get_attribute('href')
                        channel_link=i.find_element(By.CSS_SELECTOR,'#channel-info .ytd-channel-name a').get_attribute('href')
                        channel_name=i.find_element(By.CSS_SELECTOR,'#channel-info .ytd-channel-name a').text
                        x = YouTube(video_link)
                        
                        channel_id=x.channel_id
                        """
                        try:
                            request = youtube.search().list(channelId=channel_id, type='channel', part='id', maxResults=1)
                            response = request.execute()
                        except Exception as e:
                                print(e)
                                break    
                        channel_id = response['items'][0]['id']['channelId']

                        # Use the channel ID to get the channel statistics
                        request = youtube.channels().list(part='statistics', id=channel_id)
                        response = request.execute()
                        view_count=response['items'][0]['statistics']['viewCount']
                        subscriber_count=response['items'][0]['statistics']['subscriberCount']
                        video_count=response['items'][0]['statistics']['videoCount']
                        """
                        
                        search_driver.get(channel_link+'/about')  # Replace with your desired URL
                        time.sleep(3)
                        
                        view_count=search_driver.find_element(By.XPATH,'/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-engagement-panel-section-list-renderer/div[2]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-about-channel-renderer/div/div[5]/table/tbody/tr[6]/td[2]').text.strip('\n')
                        subscriber_count=search_driver.find_element(By.XPATH,'/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-engagement-panel-section-list-renderer/div[2]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-about-channel-renderer/div/div[5]/table/tbody/tr[4]/td[2]').text.strip('\n')
                        video_count=search_driver.find_element(By.XPATH,'/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-engagement-panel-section-list-renderer/div[2]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-about-channel-renderer/div/div[5]/table/tbody/tr[5]/td[2]').text.strip('\n')
                        try:
                            email_search=search_driver.find_element(By.XPATH,'//*[@id="view-email-button-container"]')
                            email_has='Yes'
                        except:
                            email_has='No'
                        text_description=search_driver.find_element(By.XPATH,'//*[@id="description-container"]').text   
                        found_emails = find_emails(text_description) 
                        if(len(found_emails)>0):
                            email_in_description=",".join(found_emails)
                        else:
                            email_in_description="No"
                            
                                
                        social_media_links=search_driver.find_element(By.CSS_SELECTOR,'#link-list-container').find_elements(By.CSS_SELECTOR,'a')
                        social_media_url_list=[]
                        if(len(social_media_links)>0):
                                    for i in social_media_links:
                                        redirecturl=i.get_attribute('href')
                                        social_media_url=get_social_media_link(redirecturl)
                                        if(social_media_url!=None):
                                                social_media_url_list.append(social_media_url)
                                    if(len(social_media_url_list)>0):            

                                            social_media=",".join(social_media_url_list)
                                    else:
                                                social_media="None"
                                                            
                        else:
                                social_media="None"            

                                    
                            
                        
                        
                        if channel_id not in data:
                                                        writer.writerow([channel_id, channel_name, channel_link, view_count,subscriber_count,video_count,email_has,email_in_description,social_media])
                                                        print(f"Channel ID: {channel_id}, Channel name: {channel_name}, Channel url: {channel_link}, View Count: {view_count} ,Subscriber Count: {subscriber_count} ,Video Count: {video_count} ,Email has?: {email_has} ,Email in description? :{email_in_description} ,Social media :{social_media}")
                                                        data.add(channel_id)

                    except KeyboardInterrupt:
                                print(f'Aborted. Keyboard Interrupt') 
                                break
                    except Exception as e:
                            print(e)
                            break

file.close()                                
search_driver.quit() 
print('Finshed scraping. Please check your output file.') 
driver.quit()                                              