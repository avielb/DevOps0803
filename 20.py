from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

my_driver = webdriver.Chrome(executable_path="/Users/avielb/Downloads/chromedriver")
my_driver.implicitly_wait(5)
expected = "5.00"
my_driver.get("file:///Users/avielb/Downloads/tip_calc/index.html")
my_driver.find_element_by_id("billamt").send_keys("100")
sleep(2)
my_driver.find_element_by_xpath('//*[@id="serviceQual"]/option[3]').click()
my_driver.find_element_by_id("peopleamt").send_keys("5")
my_driver.find_element_by_id("musicAmt").send_keys("5")
my_driver.find_element_by_id("calculate").click()
actual = my_driver.find_element_by_id("tip").text
assert actual != expected
