from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Item_checkout:
    btn_checkout_xpath = "//a[@href='/demo/index.php/checkout']"
    btn_checkoutnewcust_xpath = "//button[@id='button-account']"
    txt_firstname_xpath = "//*[@id='first_name']"
    txt_lastname_xpath = "//input[@id='last_name']"
    txt_email_xpath = "//input[@id='email']"
    txt_phoneno_xpath = "//input[@id='phone_1']"
    txt_mobileno_xpath = "//input[@id='phone_2']"
    txt_password_css = "div[class='col-md-6'] input[name='password']"
    txt_cnfrmpsswrd_xpath = "//input[@name='confirm']"
    txt_company_xpath = "//input[@id='company']"
    txt_taxnumbr_xpath = "//input[@id='tax_number']"
    txt_addrss1_xpath = "//input[@id='address_1']"
    txt_addrss2_xpath = "//input[@id='address_2']"
    txt_city_xpath = "//input[@id='city']"
    txt_zipcode_xpath = "//input[@id='zip']"
    drpdwn_allcountry_xpath = "//select[@id='country_id']"
    drpdwn_allregion_xpath = "//select[@id='zone_id']"
    btn_continuetopayments_xpath = "//input[@id='button-register']"
    rdbtn_cashondelivry_xpath = "//div[@id='shipping-payment-method']/div[2]/div[1]/div[2]/label"
    btn_continuecnfrm_xpath = "//input[@id='button-payment-method']"
    btn_placeorder_xpath = "//div[@class='payment']/form/input[1]"
    link_gotoorderhistry_xpath = "//div[@class='col-md-12']/div[2]/a"



    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(By.XPATH, self.btn_checkout_xpath).click()

    def click_checkotasnewcust(self):
        self.driver.find_element(By.XPATH, self.btn_checkoutnewcust_xpath).click()

    def set_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(firstname)

    def set_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.txt_lastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_lastname_xpath).send_keys(lastname)

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def set_phoneno(self, phoneno):
        self.driver.find_element(By.XPATH, self.txt_phoneno_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_phoneno_xpath).send_keys(phoneno)

    def set_mobileno(self, mobileno):
        self.driver.find_element(By.XPATH, self.txt_mobileno_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_mobileno_xpath).send_keys(mobileno)

    def set_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.txt_password_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.txt_password_css).send_keys(password)

    def set_cnfrmpasswrd(self, cnfrmpasswrd):
        self.driver.find_element(By.XPATH, self.txt_cnfrmpsswrd_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_cnfrmpsswrd_xpath).send_keys(cnfrmpasswrd)

    def set_companyname(self, cmpnyname):
        self.driver.find_element(By.XPATH, self.txt_company_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_company_xpath).send_keys(cmpnyname)

    def set_taxnumber(self, taxnumber):
        self.driver.find_element(By.XPATH, self.txt_taxnumbr_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_taxnumbr_xpath).send_keys(taxnumber)

    def set_address1(self, address1):
        self.driver.find_element(By.XPATH, self.txt_addrss1_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_addrss1_xpath).send_keys(address1)

    def set_address2(self, address2):
        self.driver.find_element(By.XPATH, self.txt_addrss2_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_addrss2_xpath).send_keys(address2)

    def set_cityname(self, cityname):
        self.driver.find_element(By.XPATH, self.txt_city_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_city_xpath).send_keys(cityname)

    def set_zipcode(self, zipcode):
        self.driver.find_element(By.XPATH, self.txt_zipcode_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_zipcode_xpath).send_keys(zipcode)

    def select_country(self, country):
        countries = Select(self.driver.find_element(By.XPATH, self.drpdwn_allcountry_xpath))
        countries.select_by_visible_text(country)

    def select_region(self, region):
        regions = Select(self.driver.find_element(By.XPATH, self.drpdwn_allregion_xpath))
        regions.select_by_visible_text(region)

    def click_cashondelivery(self):
        mywait = WebDriverWait(self.driver, 10, poll_frequency=2, ignored_exceptions=NoSuchElementException)
        clickoncash = mywait.until(EC.element_to_be_clickable((By.XPATH, self.rdbtn_cashondelivry_xpath)))
        clickoncash.click()


    def clickbtncontiuetopayments(self):
        self.driver.find_element(By.XPATH, self.btn_continuetopayments_xpath).click()


    def clickcontinuetoconfrm(self):
        self.driver.find_element(By.XPATH, self.btn_continuecnfrm_xpath).click()

    def clicktoplaceorder(self):
        self.driver.find_element(By.XPATH, self.btn_placeorder_xpath).click()

    def click_orderhistory(self):
        self.driver.find_element(By.XPATH, self.link_gotoorderhistry_xpath).click()
