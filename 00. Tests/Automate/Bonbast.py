from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.bonbast.com/')

usd1 = browser.find_element(By.ID, "usd1")
usd2 = browser.find_element(By.ID, "usd2")

print("Sell", usd1.text)
print("Buy", usd2.text)
