import data
from selenium import webdriver
from helpers import retrieve_phone_code
from pages import UrbanRoutesPage

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # Configure ChromeDriver to capture network logs
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.wait_until_loaded()
        address_from = data.address_from
        address_to = data.address_to

        # Fill in the route and assert it's correctly set
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_comfort(self):
        # Select ride option
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort()
        comfort_button = self.driver.find_element(*routes_page.element_comfort)
        assert "active" in comfort_button.get_attribute("class"), "Comfort button was not activated"

    def test_set_phone_number(self):
        # Enter phone number and confirm with code
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        number = data.phone_number
        routes_page.set_number(number)
        code = retrieve_phone_code(self.driver)
        routes_page.set_code(code)
        assert routes_page.get_phone_number() == number


    def test_add_credit_card(self):
        # Add credit card details
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        number = data.card_number
        code = data.card_code
        routes_page.set_card(number, code)
        assert routes_page.get_card_number() == number

    def test_add_comment(self):
        # Add custom comment
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        comment = data.message_for_driver
        routes_page.set_comment(comment)
        assert routes_page.get_comment() == comment

    def test_add_requests(self):
        # Add ride requirements
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_requests()
        ice_cream_counter = self.driver.find_element(*routes_page.icecream_counter)
        assert ice_cream_counter.text == "2"
        switch = self.driver.find_element(UrbanRoutesPage.blanket_tissues)
        assert switch.is_selected(), "El switch de 'Manta y pañuelos' debería estar activado, pero no lo está."


    def test_order_taxi(self):
        # Confirm "Order Taxi" button text
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        modal = routes_page.order_taxi_displayed()
        assert modal == "Pedir un taxi", f"Unexpected button text: '{modal}'"

    def test_modal_driver(self):
        # Click the button and wait for driver info
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        driver_name_element = UrbanRoutesPage.wait_for_driver(routes_page)
        assert driver_name_element.is_displayed(), "El nombre del conductor no se muestra en pantalla."



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
