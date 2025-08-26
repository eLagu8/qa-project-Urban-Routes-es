import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class UrbanRoutesPage:
    # Element locators
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_taxi = (By.XPATH, '//button[text()="Pedir un taxi"]')
    element_comfort = (By.XPATH, '//div[normalize-space(text())="Comfort"]')
    tag_comfort = (By.CSS_SELECTOR, '')
    element_number = (By.CLASS_NAME, 'np-text')
    phone_box = (By.ID, 'phone')
    next_button_number = (By.XPATH, '//button[text()="Siguiente"]')
    code_box = (By.ID, 'code')
    button_confirm_code = (By.XPATH, '//button[text()="Confirmar"]')
    payment_method_button = (By.CSS_SELECTOR, 'div.pp-text')
    add_card_button = (By.CLASS_NAME, 'pp-plus-container')
    card_number = (By.ID, 'number')
    code_card = (By.CSS_SELECTOR, 'input.card-input#code')
    confirm_card = (By.XPATH, '//button[text()="Agregar"]')
    close_button_payment_section = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/button')
    comment_section = (By.ID, 'comment')
    requirements_section = (By.CLASS_NAME, 'reqs-head')
    request_1 = (By.CSS_SELECTOR, "span.slider.round")
    icecream_request = (By.CSS_SELECTOR, "div.counter-plus")
    icecream_counter = (By.CSS_SELECTOR, "div.counter-value")
    blanket_tissues = (By.CSS_SELECTOR, "input.switch-input")
    order_taxi_button = (By.CLASS_NAME, 'smart-button-main')
    driver_info = (By.XPATH, "//div[text()='driver.name.1']")


    def __init__(self, driver):
        self.driver = driver

    # Enter pickup location
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    # Enter destination location
    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    # Retrieve pickup location value
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    # Retrieve destination location value
    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Enter both pickup and destination
    def set_route(self, from_address, to_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)
        self.driver.find_element(*self.to_field).send_keys(to_address)

    # Wait until main fields are visible
    def wait_until_loaded(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.from_field))
        wait.until(EC.presence_of_element_located(self.to_field))

    # Select comfort ride option
    def set_comfort(self):
        self.driver.find_element(*self.button_taxi).click()
        self.driver.find_element(*self.element_comfort).click()

    # Set phone number and go to code verification
    def set_number(self, number):
        self.driver.find_element(*self.element_number).click()
        self.driver.find_element(*self.phone_box).send_keys(number)
        self.driver.find_element(*self.next_button_number).click()

    # Retrieve phone number value
    def get_phone_number(self):
        return self.driver.find_element(*self.phone_box).get_property('value')

    # Set verification code
    def set_code(self, code):
        self.driver.find_element(*self.code_box).send_keys(code)
        self.driver.find_element(*self.button_confirm_code).click()

    # Add credit card info
    def set_card(self, number, code):
        self.driver.find_element(*self.payment_method_button).click()
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.card_number).send_keys(number)
        self.driver.find_element(*self.code_card).send_keys(code)
        self.driver.find_element(*self.code_card).send_keys(Keys.TAB)
        self.driver.find_element(*self.confirm_card).click()
        self.driver.find_element(*self.close_button_payment_section).click()

    # Retrieve card number section value
    def get_card_number(self):
        return self.driver.find_element(*self.card_number).get_property('value')

    # Add comment for the driver
    def set_comment(self, comment):
        self.driver.find_element(*self.comment_section).send_keys(comment)

    # Retrieve comment section value
    def get_comment(self):
        return self.driver.find_element(*self.comment_section).get_property('value')

    # Toggle some extra ride requirements
    def set_requests(self):
        wait = WebDriverWait(self.driver, 2)
        req_section = wait.until(EC.presence_of_element_located(self.requirements_section))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", req_section)
        self.driver.find_element(*self.request_1).click()
        self.driver.find_element(*self.icecream_request).click()
        self.driver.find_element(*self.icecream_request).click()

    # Verify the "Order Taxi" button is visible and return its text
    def order_taxi_displayed(self):
        wait = WebDriverWait(self.driver, 5)
        button = wait.until(EC.visibility_of_element_located(self.order_taxi_button))
        return button.text

    # Click order button and wait for the driver info to appear
    def wait_for_driver(self):
        self.driver.find_element(*self.order_taxi_button).click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(*self.driver_info)
        )
