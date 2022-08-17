import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture()
def setup():
    serv_obj_chrome = ChromeService(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=serv_obj_chrome)
    print("Launching chrome browser.........")
    return driver


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'j2store demo'

    config._metadata['Tester'] = 'kishan ambi'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
