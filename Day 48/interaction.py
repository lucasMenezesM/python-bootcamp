from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element(By.NAME, value="fName")
last_name_input = driver.find_element(By.NAME, value="lName")
email_input = driver.find_element(By.NAME, value="email")

first_name_input.send_keys("lucas")
last_name_input.send_keys("m")
email_input.send_keys("email@gmail.com")

email_input.send_keys(Keys.ENTER)

# articles_number = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]").text

# print(articles_number)

# driver.quit()