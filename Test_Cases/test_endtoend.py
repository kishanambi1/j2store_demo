from PageObjects import Home_page
from PageObjects import item_CheckoutPage
from Utilities.CustomLogger import LogGen
from Utilities.ReadProperties import ReadConfig
from PageObjects import AddToCartPage
import pytest
import string
import random



class Test_itemaddandchckout:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_itemaddandcheckout(self, setup):
        self.logger.info("*************** Test_005_EndToEnd *****************")
        self.logger.info("**** end to end test started ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.selectitems = Home_page.Shop_category(self.driver)
        self.logger.info("****Adding items to cart ****")
        self.selectitems.mousehovr_shpcat_tshrt()
        self.addcart = AddToCartPage.Add_ToCart(self.driver)
        self.addcart.click_addtshirt()

        self.selectitems.mousehovr_shptcat_blndrs()
        self.addcart.click_addblender()
        self.selectitems.mousehovr_shptcat_sofa()
        self.addcart.click_addsofa()
        self.logger.info("**** items added successfully to cart ****")

        self.itemscheckout = item_CheckoutPage.Item_checkout(self.driver)
        self.itemscheckout.click_checkout()
        self.itemscheckout.click_checkotasnewcust()
        self.itemscheckout.set_firstname("kishan")
        self.itemscheckout.set_lastname("ambi")
        self.email = random_generator() + "@gmail.com"
        self.itemscheckout.set_email(self.email)
        self.itemscheckout.set_phoneno(9988776655)
        self.itemscheckout.set_mobileno(9988776655)
        self.itemscheckout.set_password("password")
        self.itemscheckout.set_cnfrmpasswrd("password")
        self.itemscheckout.set_companyname("benz")
        self.itemscheckout.set_taxnumber(123456789)
        self.itemscheckout.set_address1("whitefield")
        self.itemscheckout.set_address2("bangalore urban")
        self.itemscheckout.set_cityname("bangalore")
        self.itemscheckout.set_zipcode(560047)
        self.itemscheckout.select_country("India")
        self.itemscheckout.select_region("Karnataka")
        self.itemscheckout.clickbtncontiuetopayments()

        self.itemscheckout.click_cashondelivery()
        self.itemscheckout.clickcontinuetoconfrm()

        self.itemscheckout.clicktoplaceorder()
        self.itemscheckout.click_orderhistory()
        self.logger.info("**** items added to cart and order placed ****")
        actual_title = self.driver.title
        expected_title = "My Account"
        self.logger.info("**** validating the order placed ****")
        if actual_title == expected_title:
            self.driver.close()
            self.logger.info("********* end to end Test Passed *********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "orderpage_scr.png")  # Screenshot
            self.logger.error("********* end to end Test Test Failed ************")
            self.driver.close()
            assert False


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):  # to generate random email id's
    return ''.join(random.choice(chars) for x in range(size))
