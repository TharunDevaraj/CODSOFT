from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Setup WebDriver (Chrome example)
driver = webdriver.Chrome()

def open_whatsapp_web():
    driver.get('https://web.whatsapp.com')
    print("Please scan the QR code.")
    time.sleep(25)  # Wait for user to scan QR code and log in

def find_chat(contact_name):
    search_box_xpath = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div'
    
    # Use By.XPATH to locate the search box
    search_box = driver.find_element(By.XPATH, search_box_xpath)
    search_box.click()
    search_box.send_keys(contact_name)
    time.sleep(2)  # Allow time for search results to appear
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  # Allow time for chat to open

def send_message(message):
    message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    
    # Use By.XPATH to locate the message box
    message_box = driver.find_element(By.XPATH, message_box_xpath)
    message_box.click()
    message_box.send_keys(message)
    message_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Allow time for message to send

def send_emergency_numbers(contact_name):
    emergency_numbers = {
        "TamilNadu":
        {"Police": "100",
        "Fire Department": "101",
        "Ambulance": "108",
        "Emergency Services": "112"},
        "Delhi":
        {"Police": "100",
        "Fire Department": "101",
        "Ambulance": "102",
        "Emergency Services": "112"},
        "West Bengal":
        {"Police": "100",
        "Fire Department": "101",
        "Ambulance": "102",
        "Emergency Services": "112"},
        "Maharashtra":
        {"Police": "100",
        "Fire Department": "101",
        "Ambulance": "102",
        "Emergency Services": "112"}
    }

    open_whatsapp_web()
    find_chat(contact_name)

    for region, services in emergency_numbers.items():
        message_content = f"Region: {region}\n"
        for service, number in services.items():
            message_content += f"  {service}: {number}\n"
        message_content += "\n"
        message_content+='***'
        send_message(message_content)
        time.sleep(5)  # Pause between messages

    print("Emergency numbers sent.")

# Example usage
send_emergency_numbers("Tharun")  # Replace with the name of the recipient

# Clean up
driver.quit()
