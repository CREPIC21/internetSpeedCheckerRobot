from selenium import webdriver
import time

chrome_driver_path = "your chrome driver path on your computer/laptop"
# your internet download speed promised by your service provider - used for testing
DOWN_SPEED = 150
# your internet upload speed promised by your service provider - used for testing
UP_SPEED = 20

class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        # URL for checking internet speed
        self.speed_test_url = "https://www.speedtest.net/"
        # URL for twitter Login page
        self.twitter_login = "https://twitter.com/login"
        # your twitter credentials
        self.my_email = "your twitter email login"
        self.my_password = "your twitter password login"
        self.down = 0
        self.up = 0
        
    def get_internet_speed(self):
        # getting current internet speed for your machine by bot connecting to web page
        self.driver.get(self.speed_test_url)
        time.sleep(5)
        consent_btn = self.driver.find_element_by_class_name("evidon-barrier-acceptbutton")
        consent_btn.click()
        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()
        time.sleep(60)
        self.down = float(self.driver.find_element_by_class_name("download-speed").text)
        self.up = float(self.driver.find_element_by_class_name("upload-speed").text)
    
    def tweet_to_provider(self):
        # logging to twitter account by bot with your credentials
        self.driver.get(self.twitter_login)
        time.sleep(5)
        email_input = self.driver.find_element_by_css_selector('[name="session[username_or_email]"]')
        email_input.send_keys(self.my_email)
        password_input = self.driver.find_element_by_css_selector('[name="session[password]"]')
        password_input.send_keys(self.my_password)
        login_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        login_btn.click()
        time.sleep(3)
        # checking if your internet speed is slower then internet service provider promised
        # if the speed is slower bot will post complain tweet
        if self.down < DOWN_SPEED or self.up < UP_SPEED:
            msg = f"Hello Internet Provider, why is my internet speed {self.down}down/{self.up}up when I am paying for {DOWN_SPEED}down/{UP_SPEED}up?"
            tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/span/br')
            tweet.send_keys(msg)
            tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div')
            tweet_btn.click()
            time.sleep(5)
        self.driver.quit()
