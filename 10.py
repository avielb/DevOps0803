import requests
from selenium import webdriver
from time import sleep
for i in range(5):
    result = requests.get("https://github.com")
    if result.status_code != 200:
        print("GitHub is down")
        break
    sleep(5)
else:
    print("GitHub was ok")
