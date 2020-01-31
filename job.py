from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import csv
import sys

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class HandleBrowser():
    
    CONTENT_LIST = [{'content_type': 'text', 'data': 'Lorem ipsum'}] 


    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage");
        self.chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "safebrowsing-disable-download-protection", "safebrowsing-disable-auto-update", "disable-client-side-phishing-detection"])
        self.chrome_options.add_argument("user-data-dir=/home/lenovo/.config/google-chrome/Default") #Path to your chrome profile
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get('https://www.naukri.com/mnjuser/recommendedjobs')
        self.argument = sys.argv 



    def scrape_page(self):
        pass

    def  scrap_post(self):
        try:
            images = self.driver.find_elements_by_xpath("//article [@class='jobTuple bgWhite br4 z-depth-1 pl-18']")
            with open('job.csv', mode='w') as facebook_file:
                scrape_data = csv.writer(facebook_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for image in images:
                    post_id = image.get_attribute("data-job-id")
                    post_text = image.text
                    scrape_data.writerow([post_id, post_text])

        except:
            pass

if __name__ == '__main__':
    browser = HandleBrowser()
    
    for arg in browser.argument:
        if arg == 'scrap_post':
            browser.scrap_post()

        if arg == 'scrape_page':
            browser.scarping_post()
      