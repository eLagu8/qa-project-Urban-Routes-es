
# Urban Routes Automated Testing

This repository contains automated end-to-end tests for the **Urban Routes** web application using **Selenium** and **Pytest**. The goal is to validate the complete process of ordering a taxi, ensuring that key user interactions behave as expected.

## 📁 Project Structure

```
urban_routes_test/
│
├── main.py          # Main test file containing all test logic
├── pages.py        # Contains all localizators and functionalities
├── helpers.py      # Contain a function for retrieving a code of verification
├── README.md        # Project documentation

```

## 🧪 Test Overview

All the automated tests are defined in `main.py`, structured into two main classes:

- `TestUrbanRoutes`: Contains the test case that simulates a user ordering a taxi, step-by-step.

## 🧪 File pages.py with class UrbanRoutesPage 
- `UrbanRoutesPage`: Contains the page object model (POM) logic — locators and methods to interact with UI elements.

## ✅ Test Scenario – "Order a Taxi"

The automated test simulates the following actions in the Urban Routes app:

1. **Configure Address**  
   _Already implemented as a reference._

2. **Select Comfort Fare**  
   Locates and selects the "Comfort" tariff button.

3. **Fill in Phone Number**  
   Inputs a valid number and handles confirmation code retrieval.

4. **Add Credit Card**  
   Opens the "Add Card" modal, inputs card details, and handles field blur with `TAB` to enable the submit button.  
   > The field loses focus via `TAB` to activate the "Link" button.

5. **Write a Note to the Driver**  
   Sends a custom message for the driver.

6. **Add Ride Requirements**  
   Selects additional requests such as:
   - "Pedir una manta y pañuelos" (Ask for a blanket and tissues)
   - "Pedir 2 helados" (Ask for 2 ice creams)

7. **Open the 'Searching for Taxi' Modal**  
   Triggers the modal that starts searching for a driver.

8. **Wait for Driver Information (Optional)**  
   Waits for up to 25 seconds while the app searches for a driver. When a driver is assigned, their information is displayed.  
   > Useful to test real-world async behavior like timeouts or delays.

## 🚀 Running the Test

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the test using Pytest:
   ```bash
   pytest main.py
   ```

## 🔍 Notes

- Uses `WebDriverWait` for all critical steps to ensure elements are interactable.
- JavaScript scrolls and waits are used where elements are off-screen or delayed.
- Test stability relies on realistic delays and proper element focus handling.

## 🧰 Technologies

- **Python 3.11+**
- **Selenium**
- **Pytest**

## ✍️ Author

Test logic and automation created for TripleTen QA Project – Urban Routes. By Eduardo Lagunas Cohort 32QA
