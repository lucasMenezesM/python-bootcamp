from selenium import webdriver
from selenium.webdriver.common.by import By

class CookieBot:
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://orteil.dashnet.org/experiments/cookie/")

        self.cookie = self.driver.find_element(By.XPATH, '//*[@id="cookie"]')
        self.cookie_count = self.driver.find_element(By.XPATH, '//*[@id="money"]').text

        right_panel_html = self.driver.find_element(By.CSS_SELECTOR, "#rightPanel #store")
        self.right_panel = right_panel_html.find_elements(By.CSS_SELECTOR, 'div')


    def click_cookie(self) -> None:
        """Clicks the cookie a single time"""
        self.cookie.click()


    def get_price(self, element) -> float:
        """Returns the price of a given element"""

        price = element.text.split("-")[1].split("\n")[0].strip()
        if "," in price:
            price = price.replace(",", "")
        return float(price)


    def get_cookie_count(self) -> float:
        """Returns the cookie count"""
        cookie_count = self.driver.find_element(By.XPATH, '//*[@id="money"]').text
        return float(cookie_count)


    def check_available_elements(self) -> list:
        """Returns a list with the available elements in the right panel for purchase"""

        available_elements = []
        for element in self.right_panel:
            if element.get_attribute("class") != "grayed":
                available_elements.append(element)

        return available_elements
    

    def buy_powerup(self):
        """Buys the available element with the higher price"""

        current_money = self.get_cookie_count()
        elements_to_buy = []
        
        for element in self.right_panel:
            if len(element.text) > 0:
                # print(element.text)
                price = self.get_price(element)
                # print(f"Price: {price}")
                if current_money >= price:
                    elements_to_buy.append(element)

        print("Antes do IF")
        if len(elements_to_buy) > 0:
            print("DEPOIS do IF")
            print(elements_to_buy)
            # print(elements_to_buy[-1])
            elements_to_buy[0].click()
        else:
            print("not enough money")


    def buy_element(self):
        """Buys the available element with the higher price"""

        elements = self.check_available_elements()
        if len(elements) == 0:
            print("purchase is not available")
            return
        
        higher_price = 0
        element_to_buy = None

        for element in elements:

            if element.text:
                price = element.text.split("-")[1].split("\n")[0].strip()
                if "," in price:
                    price = price.replace(",", "")

                if float(price) > higher_price:
                    higher_price = float(price)
                    element_to_buy = element


        element_to_buy.click()
