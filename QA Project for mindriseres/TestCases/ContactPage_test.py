from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import time
from PageObjects.ContactPage import ContactPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test001Contact:
    baseUrl = ReadConfig.geturl()
    name = ReadConfig.getname()
    email = ReadConfig.getemail()
    phone = ReadConfig.getphone()
    interest = ReadConfig.getinterest()
    company = ReadConfig.getcompany()
    queries = ReadConfig.getany_queries()
    logger = LogGen.loggen()

    def test_contactus(self, setup):
        self.logger.info("***** Test001Contact - Contact Us Form Test *****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseUrl)

        self.cp = ContactPage(self.driver)
        self.cp.click_contact()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 4);")
        time.sleep(3)  # Allow scroll or navigation animation if needed

        self.cp.enter_name(self.name)
        time.sleep(3)
        self.cp.enter_email(self.email)
        self.cp.enter_phone(self.phone)
        time.sleep(3)
        self.cp.enter_interest(self.interest)
        self.cp.enter_company_name(self.company)
        time.sleep(3)
        self.cp.enter_queries(self.queries)
        time.sleep(3)
        self.cp.click_on_submit()
        time.sleep(3)

        try:
            self.logger.info("*** Checking if Contact form heading is visible ***")

            # Wait for the heading <p class='title'> to appear
            heading_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[@class='title']"))
            )

            heading_text = heading_element.text.strip()
            self.logger.info(f"*** Heading found: '{heading_text}' ***")

            # ✅ Assert the heading contains expected phrase (modify as needed)
            assert "Have a Project" in heading_text or "Contact" in heading_text, "Unexpected heading text!"

        except Exception as e:
            screenshot_path = ".//Screenshots/test_contact_form_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"**** Contact test failed: {str(e)}. Screenshot saved at {screenshot_path} ****")
            assert False

        finally:
            self.driver.quit()




