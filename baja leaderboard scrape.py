from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialize WebDriver (Ensure you have chromedriver installed)
driver = webdriver.Chrome()
url = "https://results.bajasae.net/Leaderboard.aspx"
driver.get(url)

# Wait for the dropdown to be available
dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "MainContent_DropDownListEvents"))
)

# Select an event from the dropdown
select = Select(dropdown)
select.select_by_visible_text("Endurance")  # Replace with the exact event name

# Click the "Show Most Recent Results" button if needed
show_results_btn = driver.find_element(By.ID, "MainContent_ButtonLookupEvent")
show_results_btn.click()

# Wait for the table to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "table"))
)

# Get page source and parse with BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Find the table
tables = soup.find_all("table")

# Extract data from table rows
data = []
for table in tables:
    if table:
        
        headers = [th.text.strip() for th in table.find_all("th")]
        
        rows = table.find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            cols = [col.text.strip() for col in cols]
            if cols:  # Avoid empty rows
                data.append(cols)

# Print extracted data
search_string = "Virginia Tech"
print("first place")

for row in data:
    
        # Strip spaces and ensure the comparison works correctly
        if row[0].strip() == "1":
            for idx, value in enumerate(row):
                print(f"{headers[idx]}: {value}")
        
   

print("\n\n\nsearched value")

for row in data:
    # Check if row contains the search string
    if any(search_string in col for col in row):
        for idx, value in enumerate(row):
            print(f"{headers[idx]}: {value}")


# Close the driver
driver.quit()
