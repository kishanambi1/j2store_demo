import pytest
from PageObjects import Home_page
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import LogGen



class Test_001_category:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_HomePage *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title

        if act_title == "Home":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_search_tshirt(self, setup):
        self.logger.info("*************** Test_002_Search_T-shirt *****************")
        self.logger.info("****Started tshirt in shop category test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.homep = Home_page.Shop_category(self.driver)
        self.homep.mousehovr_shpcat_tshrt()

        self.logger.info("********* tshirt in shop category validation started *****************")
        if self.driver.title == "T-Shirts":
            self.driver.close()
            self.logger.info("********* tshirt in shop category Test Passed *********")
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "tshirt_in_shop_category_scr.png")  # Screenshot
            self.logger.error("********* tshirt in shop category Test Failed ************")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_search_blenders(self, setup):
        self.logger.info("*************** Test_003_Search_blenders *****************")
        self.logger.info("****tshirt in shop category test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.homep = Home_page.Shop_category(self.driver)

        self.homep.mousehovr_shptcat_blndrs()

        self.logger.info("********* blenders in shop category validation started *****************")

        if self.driver.title == "Blenders":
            self.driver.close()
            self.logger.info("********* blenders in shop category Test Passed *********")
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "blenders_in_shop_category_scr.png")  # Screenshot
            self.logger.error("********* blenders in shop category Test Failed ************")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_search_sofa(self, setup):
        self.logger.info("*************** Test_004_Search_Sofa *****************")
        self.logger.info("****sofa in shop category test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.homep = Home_page.Shop_category(self.driver)

        self.homep.mousehovr_shptcat_sofa()

        self.logger.info("********* sofa in shop category validation started *****************")

        if self.driver.title == "Sofa":
            self.driver.close()
            self.logger.info("********* sofa in shop category Test Passed *********")
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "sofa_in_shop_category_scr.png")  # Screenshot
            self.logger.error("********* sofa in shop category Test Failed ************")
            self.driver.close()
            assert False





