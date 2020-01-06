from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
# import urllib.request 
import csv
# import validators
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
        self.driver.get('https://www.facebook.com/')
        self.argument = sys.argv 


    def login(self):        
        username = "xyz@gmail.com"
        password = "password"
         
        a = self.driver.find_element_by_id('email')  
        a.send_keys(username) 
        time.sleep(5)
        # password send 
        b = self.driver.find_element_by_id('pass')  
        b.send_keys(password) 
        time.sleep(5)
          
        # submit button clicked 
        self.driver.find_element_by_id('loginbutton').click() 

    def  publish_post(self):

        msg = "WelCome to Webllisto Family ,We provide expert web advancement solutions 10."
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath("//textarea[@name='xhpc_message']").send_keys(msg)
            time.sleep(5)
            self.driver.find_element_by_xpath("//*[text()='Post']").click()
            time.sleep(5)
        except :
            pass
        self.scarping_post()

    def scarping_post(self):

        self.driver.get('https://www.facebook.com/')
        try:
            posts =  self.driver.find_elements_by_xpath("//div [@data-testid='post_message']")
            with open('facebook.csv', mode='w') as facebook_file:
                scrape_data = csv.writer(facebook_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for post in posts:
                    post1 = post.text
                    ids = post.id
                    employee_writer.writerow([ids, post1])
        except:
            pass
        self.comment_on_post()

    def comment_on_post(self):

        self.driver.get('https://www.facebook.com/andrew.jhon.90834/posts/101114511421112')
        try:
            self.driver.find_element_by_class_name("_7c-t").click()            
            time.sleep(5)
            self.driver.find_element_by_class_name("_1mf").send_keys("Nice... ")
            time.sleep(5)
            self.driver.find_element_by_class_name("_1mf").send_keys(Keys.ENTER)
        except:
            pass
        self.like_on_post()

    def like_on_post(self):

        self.driver.get('https://www.facebook.com/andrew.jhon.90834/posts/101114511421112')
        try:
            self.driver.find_element_by_class_name("_666k").click()
        except:
            pass
        self.replied_comment()


    def logout(self):
        try:
            self.driver.find_element_by_class_name("_6qfu").click()
            time.sleep(2)
            self.driver.find_element_by_class_name("_64kz").click()
            self.chrome_options.add_argument("--disable-dev-shm-usage")
            time.sleep(5)
        except:
            pass
        self.close_driver()

    def close_driver(self):
        self.driver.close()


if __name__ == '__main__':
    browser = HandleBrowser()
    # browser.login()
    for arg in browser.argument:
        if arg == 'scrape_page':
            browser.scarping_post()
        if arg == 'publish_post':
            browser.publish_post()
        if arg == 'comment':
            browser.comment_on_post()
        if arg == 'like':
            browser.like_on_post()