from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class Shop_category:

    button_checkout_xpath = "//li[@class='item-142']//a[normalize-space()='Checkout']"

    mousehovr_shop_category_xpath = "//a[@itemprop='url'][normalize-space()='Shop']"
    mousehovr_tshirtcat_xpath = "//a[@itemprop='url'][normalize-space()='T-Shirts']"
    mousehovr_blenders_xpath = "//a[@itemprop='url'][normalize-space()='Blenders']"
    mousehovr_sofa_xpath = "//a[@itemprop='url'][normalize-space()='Sofa']"



    def __init__(self,driver):
        self.driver = driver



    def click_checkout(self):
        self.driver.find_element(By.XPATH,self.button_checkout_xpath).click()



    def mousehovr_shpcat_tshrt(self):
        self.shopcat = self.driver.find_element(By.XPATH,self.mousehovr_shop_category_xpath)
        self.shop_tshrt = self.driver.find_element(By.XPATH,self.mousehovr_tshirtcat_xpath)
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(self.shopcat).move_to_element(self.shop_tshrt).click().perform()

    def mousehovr_shptcat_blndrs(self):
        self.shopcat = self.driver.find_element(By.XPATH, self.mousehovr_shop_category_xpath)
        self.shop_blndrs = self.driver.find_element(By.XPATH,self.mousehovr_blenders_xpath)
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(self.shopcat).move_to_element(self.shop_blndrs).click().perform()

    def mousehovr_shptcat_sofa(self):
        self.shopcat = self.driver.find_element(By.XPATH, self.mousehovr_shop_category_xpath)
        self.shop_sofa = self.driver.find_element(By.XPATH,self.mousehovr_sofa_xpath)
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(self.shopcat).move_to_element(self.shop_sofa).click().perform()





