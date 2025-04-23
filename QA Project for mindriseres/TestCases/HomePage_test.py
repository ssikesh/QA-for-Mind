import pytest
import time
from PageObjects.HomePage import HomePage
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class Test_HomePage:
    logger = LogGen.loggen()

    def test_homepage_navigation(self):
        self.logger.info("***** Test: Navigation on HomePage *****")
        self.driver.get("https://mindriserstech.com")
        homepage = HomePage(self.driver)
        title = homepage.get_title()
        self.logger.info(f"Home Page Title: {title}")
        assert "Mindrisers" in homepage.get_title(), "Title doesn't contain 'Mindrisers'!"


    def test_services_navigation(self):
        self.logger.info("***** Test: Navigation to Services Page *****")
        self.driver.get("https://mindriserstech.com")
        homepage = HomePage(self.driver)
        homepage.click_services()
        time.sleep(3)  # Wait for navigation, consider using WebDriverWait in real scenario
        heading = homepage.get_services_heading()
        self.logger.info(f"Services Page Heading: {heading}")
        assert "Services" in heading, "Failed to navigate to Services page!"

    def test_about_us_navigation(self):
        self.logger.info("***** Test: Navigation to About us Page *****")
        self.driver.get("https://mindriserstech.com")
        homepage = HomePage(self.driver)
        homepage.click_about_us()
        time.sleep(3)  # Wait for navigation, consider using WebDriverWait in real scenario
        heading = homepage.get_about_us_heading()
        self.logger.info(f"Services Page Heading: {heading}")
        assert "About us" in heading, "Failed to navigate to About Us page!"

    def test_career_navigation(self):
        self.logger.info("***** Test: Navigation to Services Page *****")
        self.driver.get("https://mindriserstech.com")
        homepage = HomePage(self.driver)
        homepage.click_career()
        time.sleep(3)  # Wait for navigation, consider using WebDriverWait in real scenario
        heading = homepage.get_career_heading()
        self.logger.info(f"Services Page Heading: {heading}")
        assert "Career" in heading, "Failed to navigate to Career page!"

    def test_blogs_navigation(self):
        self.logger.info("***** Test: Navigation to Blogs Page *****")
        self.driver.get("https://mindriserstech.com")
        homepage = HomePage(self.driver)
        homepage.click_blogs()
        time.sleep(3)  # Wait for navigation, consider using WebDriverWait in real scenario
        heading = homepage.get_blogs_heading()
        self.logger.info(f"Services Page Heading: {heading}")
        assert "Blogs" in heading, "Failed to navigate to Blogs page!"

    def test_technology_navigation(self):
        self.logger.info("***** Test: Navigation to Technology Page *****")
        self.driver.get("https://mindriserstech.com")
        homepage = HomePage(self.driver)
        homepage.click_technology()
        time.sleep(3)
        heading = homepage.get_technology_heading()
        self.logger.info(f"Technology Page Heading: {heading}")
        assert "Technology" in heading, "Failed to navigate to Technology page!"

    def test_portfolio_navigation(self):
        self.logger.info("***** Test: Navigation to Portfolio Page *****")
        self.driver.get("https://mindriserstech.com")
        homepage = HomePage(self.driver)
        homepage.click_portfolio()
        time.sleep(3)
        heading = homepage.get_portfolio_heading()
        self.logger.info(f"Portfolio Page Heading: {heading}")
        assert "Our Portfolio" in heading, "Failed to navigate to Portfolio page!"

