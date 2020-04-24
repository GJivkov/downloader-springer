from selenium import webdriver
import time
import pyautogui

links = []
i = 0
page_number = 1
pages_to_iterate = 39

pyautogui.PAUSE = 1

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome("D:\\Chromedriver\\chromedriver.exe", options=options)
driver.get(r"https://link.springer.com/search/page/1?package=mat-covid19_textbooks&facet-language=%22En%22&facet-content-type=%22Book%22&sortOrder=newestFirst")

while page_number < pages_to_iterate:
    driver.find_elements_by_css_selector("a[href*='/book/']")[i].click()

    driver.implicitly_wait(10)
    
    pdf = driver.find_element_by_css_selector("a[href*='/content/pdf/']")
    
    link = pdf.get_attribute("href")
    links.append(link)

    # Returns back to the page containing 10 books.
    driver.back()

    # Page change by using page_number and hard-coded link.
    if i == 9:
        time.sleep(5)
        page_number+=1

        driver.get("https://link.springer.com/search/page/" + str(page_number) + "?package=mat-covid19_textbooks&facet-language=%22En%22&facet-content-type=%22Book%22&sortOrder=newestFirst")
        
        time.sleep(5)
        i = -1

    i+=1

# iterates over the list of collected links and
# downloads every book with pyautogui (changes may be needed depending on screen resolution)

for link in links:
    driver.get(link)
    
    time.sleep(15)

    pyautogui.moveTo(100, 200)
    pyautogui.click(1751, 139) 
    pyautogui.click(803, 505)

    time.sleep(3)