import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAutomation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.saucedemo.com/"
        self.driver.get(self.url)
        time.sleep(4)

    def tearDown(self):
        self.driver.quit()

    def login(self, username, password):
        username_field = self.driver.find_element(By.ID, "user-name")
        username_field.send_keys(username)

        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        time.sleep(4)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        time.sleep(4)

    def click_add_to_cart(self, product_ids):
        for product_id in product_ids:
            add_to_cart_button = self.driver.find_element(By.ID, product_id)
            add_to_cart_button.click()
            time.sleep(3)

    def complete_checkout(self):
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        time.sleep(3)

        remove_button = self.driver.find_element(By.ID, "remove-sauce-labs-bike-light")
        remove_button.click()
        time.sleep(3)

        continue_shopping_button = self.driver.find_element(By.ID, "continue-shopping")
        continue_shopping_button.click()
        time.sleep(3)

        add_to_cart_onesie_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        add_to_cart_onesie_button.click()
        time.sleep(3)

        remove_backpack_button = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        remove_backpack_button.click()
        time.sleep(3)

        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        time.sleep(3)

        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()
        time.sleep(3)

        first_name_field = self.driver.find_element(By.ID, "first-name")
        first_name_field.send_keys("Jarvis")

        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Stark")

        postal_code_field = self.driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys("12345678")

        time.sleep(3)  

        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()
        time.sleep(3)

        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()
        time.sleep(3)

        back_home_button = self.driver.find_element(By.ID, "back-to-products")
        back_home_button.click()
        time.sleep(3)

        menu_button = self.driver.find_element(By.CLASS_NAME, "bm-burger-button")
        menu_button.click()
        time.sleep(3)

        logout_button = self.driver.find_element(By.ID, "logout_sidebar_link")
        logout_button.click()
        time.sleep(3)

    def test_regression(self):
        self.login("standard_user", "secret_sauce")
        
        product_ids = ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bike-light", "add-to-cart-sauce-labs-bolt-t-shirt", "add-to-cart-sauce-labs-fleece-jacket"]
        self.click_add_to_cart(product_ids)

        self.complete_checkout()

if __name__ == "__main__":
    unittest.main()
