from selenium import webdriver
from selenium.webdriver.common.keys import Keys
my_driver = webdriver.Chrome(executable_path="/Users/avielb/Downloads/chromedriver")
my_driver.get("https://github.com")
my_driver.find_element_by_name("q").send_keys("devops" + Keys.ENTER)