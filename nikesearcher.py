from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def get_air_jordans_on_sale():
    url = "https://www.nike.com/w/sale-3yaep"

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)

    # Set up Chrome WebDriver
    chrome_path = "/Users/taseen/Downloads/chromedriver_mac_arm641/chromedriver"  # Replace with the path to your chromedriver executable
    driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)

    # Load the URL
    driver.get(url)

    # Wait for dynamic content to load (adjust wait time as needed)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'product-card__title')))

    # Get the page source after dynamic content has loaded
    page_source = driver.page_source

    # Parse the HTML content of the page
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract information about Air Jordans on sale
    air_jordans = soup.find_all('div', class_='product-card')  # Adjust class based on Nike's HTML structure

    for jordan in air_jordans:
        # Extract relevant information (e.g., product name, price)
        product_name = jordan.find('div', class_='product-card__title').text.strip()
        price = jordan.find('div', class_='product-price').text.strip()

        # Extract all available sizes if sizes container is present
        sizes_container = jordan.find('div', class_='css-1a59uem-Sizes')
        
        if sizes_container:
            available_sizes = [size.text.strip() for size in sizes_container.find_all('button')]
            print(f"Product: {product_name}\nPrice: {price}\nAvailable Sizes: {', '.join(available_sizes)}\n---")
        else:
            print(f"Product: {product_name}\nPrice: {price}\nAvailable Sizes: Not Available\n---")

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    get_air_jordans_on_sale()