from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from cookie_bot import CookieBot

bot = CookieBot()

timeout = 300   # [seconds]
timeout_start = time.time()
interval = 5    # Intervalo de tempo para realizar a ação [seconds]
last_action_time = timeout_start

while time.time() < timeout_start + timeout:

    bot.click_cookie()

    if time.time() >= last_action_time + interval:
        print("time to buy")
        # bot.buy_element()
        # print(bot.right_panel)
        bot.buy_powerup()
        last_action_time = time.time()

    time.sleep(0.01)

# time_window = 5
# if time.time() == time.time() + time_window:
#     bot.buy_element()

# for i in range(140):
#     bot.click_cookie()


bot.buy_element()

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://orteil.dashnet.org/experiments/cookie/")

# cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
# cookie_count = driver.find_element(By.XPATH, '//*[@id="money"]').text

# # for i in range(20):
# #     cookie.click()

# # time.sleep(3)

# right_panel = driver.find_element(By.CSS_SELECTOR, "#rightPanel #store")
# right_panel = right_panel.find_elements(By.CSS_SELECTOR, 'div')

# for element in right_panel:
#     if element.text:
#         price = element.text.split("-")[1].split("\n")[0].strip()
#         if "," in price:
#             price = price.replace(",", "")

#             # parts = price.split('.')
#             # if len(parts) > 2:  # Isso significa que há pontos como separadores de milhar
#             #     price = ''.join(parts[:-1]) + '.' + parts[-1]
         
#         print(float(price))

# print(cookie_count)

# events_list_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu li a")
# events_list_datetime = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu li time")

# upcoming_events_dic = {}

# for i in range(len(events_list_name)):
#     upcoming_events_dic[i] = {
#         "time": events_list_name[i].text,
#         "name": events_list_datetime[i].text
#     }

# print(upcoming_events_dic)
# driver.quit()

# events_list_html_name = driver.find_elements(By.CSS_SELECTOR, ".shrubbery .menu li time")

# driver.get("https://www.hltv.org/")
# text = driver.find_element(By.CLASS_NAME, value="newsheader")
# print(text.text)
# driver.quit()
# print(price)
# driver.get("https://translate.google.com/?sl=en&tl=pt&text=so%20so%0Amore%20or%20so%0A&op=translate")