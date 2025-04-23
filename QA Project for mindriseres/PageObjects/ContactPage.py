from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage:
    contact_button_xpath = "//a[@class='btn-light ']"
    name_textbox_xpath = "//input[@name='full_name']"
    email_textbox_xpath = "//input[@name='email']"
    phone_textbox_xpath = "//input[@name='number']"
    interest_textbox_xpath = "//input[@name='interest']"
    company_name_textbox_xpath = "//input[@name='company_name']"
    queries_textbox_xpath = "//textarea[@name='message']"
    submit_button_xpath = "//button[normalize-space()='Send Enquiry']"
    contact_heading_xpath = "//p[@class='title']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_contact(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.contact_button_xpath))).click()

    def enter_name(self, name):
        name_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.name_textbox_xpath)))
        name_field.clear()
        name_field.send_keys(name)

    def enter_email(self, email):
        email_field = self.driver.find_element(By.XPATH, self.email_textbox_xpath)
        email_field.clear()
        email_field.send_keys(email)

    def enter_phone(self, phone):
        phone_field = self.driver.find_element(By.XPATH, self.phone_textbox_xpath)
        phone_field.clear()
        phone_field.send_keys(phone)

    def enter_interest(self, interest):
        field = self.driver.find_element(By.XPATH, self.interest_textbox_xpath)
        field.clear()
        field.send_keys(interest)

    def enter_company_name(self, company_name):
        field = self.driver.find_element(By.XPATH, self.company_name_textbox_xpath)
        field.clear()
        field.send_keys(company_name)

    def enter_queries(self, queries):
        field = self.driver.find_element(By.XPATH, self.queries_textbox_xpath)
        field.clear()
        field.send_keys(queries)

    def click_on_submit(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

    def get_success_message(self):
        return self.driver.find_element(By.XPATH, self.success_message_xpath).text
