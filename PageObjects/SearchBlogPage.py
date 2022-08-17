from selenium.webdriver.common.by import By


class SearchBlogs:

    link_blog_xpath = "//a[@itemprop='url'][normalize-space()='Blog']"
    link_siteorigin_xpath = "//a[@title='Homepage using SiteOrigin Page Builder']"
    link_remotewrk_xpath = "//a[@title='The Power Of A Remote Working Team']"

    def __init__(self, driver):
        self.driver = driver

    def click_blog(self):
        self.driver.find_element(By.XPATH, self.link_blog_xpath).click()

    def click_siteoriginpage(self):
        self.driver.find_element(By.XPATH,self.link_siteorigin_xpath).click()

    def click_remoteewrk(self):
        self.driver.find_element(By.XPATH,self.link_remotewrk_xpath).click()


