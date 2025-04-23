from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    homepage_title_xpath = "//h1"
    services_link_xpath = "//a[normalize-space()='services']"
    services_heading_xpath = "//p[normalize-space()='Services']"

    portfolio_link_xpath = "//a[normalize-space()='portfolio']"
    portfolio_heading_xpath ="//p[normalize-space()='Our Portfolio']"

    technology_link_xpath = "//a[normalize-space()='technology']"
    technology_heading_xpath = "//p[@class='title']"

    about_us_link_xpath = "//a[normalize-space()='about us']"
    about_us_heading_xpath = "//p[normalize-space()='About us']"

    blogs_link_xpath = "//a[normalize-space()='blogs']"
    blogs_heading_xpath = "//p[@class=' title text-shrink text-center']"

    career_link_xpath = "//a[normalize-space()='career']"
    career_heading_xpath = "//p[normalize-space()='Career']"


    def get_title(self):
        return self.driver.title

    def click_services(self):
        self.driver.find_element(By.XPATH, self.services_link_xpath).click()

    def get_services_heading(self):
        return self.driver.find_element(By.XPATH, self.services_heading_xpath).text

    def click_portfolio(self):
        self.driver.find_element(By.XPATH, self.portfolio_link_xpath).click()

    def get_portfolio_heading(self):
        return self.driver.find_element(By.XPATH, self.portfolio_heading_xpath).text

    def click_technology(self):
        self.driver.find_element(By.XPATH, self.technology_link_xpath).click()

    def get_technology_heading(self):
        return self.driver.find_element(By.XPATH, self.technology_heading_xpath).text

    def click_blogs(self):
        self.driver.find_element(By.XPATH, self.blogs_link_xpath).click()

    def get_blogs_heading(self):
        return self.driver.find_element(By.XPATH, self.blogs_heading_xpath).text

    def click_about_us(self):
        self.driver.find_element(By.XPATH, self.about_us_link_xpath).click()

    def get_about_us_heading(self):
        return self.driver.find_element(By.XPATH, self.about_us_heading_xpath).text

    def click_career(self):
        self.driver.find_element(By.XPATH, self.career_link_xpath).click()

    def get_career_heading(self):
        return self.driver.find_element(By.XPATH, self.career_heading_xpath).text
