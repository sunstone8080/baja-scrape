from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome()
url = "https://results.bajasae.net/Leaderboard.aspx"
driver.get(url)


dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "MainContent_DropDownListEvents"))
)


select = Select(dropdown)
select.select_by_visible_text("Endurance")  


show_results_btn = driver.find_element(By.ID, "MainContent_ButtonLookupEvent")
show_results_btn.click()


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "table"))
)


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")


tables = soup.find_all("table")


data = []
for table in tables:
    if table:
        
        headers = [th.text.strip() for th in table.find_all("th")]
        
        rows = table.find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            cols = [col.text.strip() for col in cols]
            if cols:  
                data.append(cols)


search_string = "Virginia Tech"
print("first place")

for row in data:
    
        if row[0].strip() == "1":
            for idx, value in enumerate(row):
                print(f"{headers[idx]}: {value}")
        
   

print("\n\n\nsearched value")

for row in data:
 
    if any(search_string in col for col in row):
        for idx, value in enumerate(row):
            print(f"{headers[idx]}: {value}")



driver.quit()
