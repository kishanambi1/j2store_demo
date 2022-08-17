import pytest
from PageObjects import SearchBlogPage
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from Utilities import XLUtils


class Test_Search_Blogs:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//Test_Data/Blogs_TestData.xlsx"
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_siteoriginblog(self, setup):
        self.logger.info("*************** Test_005_BlogPage *****************")
        self.logger.info("****Started SiteOrigin Page Builder in blogs test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.blogs = SearchBlogPage.SearchBlogs(self.driver)
        self.blogs.click_blog()
        self.blogs.click_siteoriginpage()

        self.siteorgn_title = XLUtils.readData(self.path, 'Sheet1', 2, 1)     # to read data from excelsheet
        self.logger.info("********* SiteOrigin Page Builder in blogs validation started *****************")

        if self.driver.title == self.siteorgn_title:
            self.driver.close()
            self.logger.info("********* SiteOrigin Page Builder in blogs Test Passed *********")
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "siteoriginpage_in_blogs_scr.png")  # Screenshot
            self.logger.error("********* SiteOrigin Page Builder in blogs Test Failed ************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_remoteorkblog(self, setup):
        self.logger.info("*************** Test_006_BlogPage *****************")
        self.logger.info("****Started Remote Working Team in blogs test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.blogs = SearchBlogPage.SearchBlogs(self.driver)
        self.blogs.click_blog()
        self.blogs.click_remoteewrk()

        self.remorewrk_title = XLUtils.readData(self.path, 'Sheet1', 3, 1)     # to read data from excelsheet

        self.logger.info("********* Remote Working Team in blogs validation started *****************")

        if self.driver.title == self.remorewrk_title:
            self.driver.close()
            self.logger.info("********* Remote Working Team in blogs Test Passed *********")
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Remote_Working_Team_in_blogs_scr.png")  # Screenshot
            self.logger.error("********* Remote Working Team in blogs Test Failed ************")
            self.driver.close()
            assert False
