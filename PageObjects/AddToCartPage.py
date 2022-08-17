from selenium.webdriver.common.by import By


class Add_ToCart:
    btnaddtshrtxpath = "//div[@id='add-to-cart-56']//input[@value='Add to cart']"
    btnaddblndrsxpath = "//div[@id='add-to-cart-60']//input[@value='Add to cart']"
    btnaddsofaxpath = "//div[@id='add-to-cart-16']//input[@value='Add to cart']"


    def __init__(self, driver):
        self.driver = driver

    def click_addtshirt(self):
        self.driver.find_element(By.XPATH, self.btnaddtshrtxpath).click()

    def click_addblender(self):
        self.driver.find_element(By.XPATH, self.btnaddblndrsxpath).click()

    def click_addsofa(self):
        self.driver.find_element(By.XPATH, self.btnaddsofaxpath).click()


