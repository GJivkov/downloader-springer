from selenium import webdriver
import time
import pyautogui

links = []

pyautogui.PAUSE = 1

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome("D:\\Chromedriver\\chromedriver.exe", options=options)
driver.get(r"https://link.springer.com/search/page/1?package=mat-covid19_textbooks&facet-language=%22En%22&facet-content-type=%22Book%22&sortOrder=newestFirst")

i = 0

page_number = 1

while page_number < 39:
    driver.find_elements_by_css_selector("a[href*='/book/']")[i].click()

    driver.implicitly_wait(10)
    
    pdf = driver.find_element_by_css_selector("a[href*='/content/pdf/']")
    
    link = pdf.get_attribute("href")
    links.append(link)

    driver.back()

    if i == 9:
        time.sleep(5)
        page_number+=1

        driver.get("https://link.springer.com/search/page/" + str(page_number) + "?package=mat-covid19_textbooks&facet-language=%22En%22&facet-content-type=%22Book%22&sortOrder=newestFirst")
        
        time.sleep(5)
        i = -1

    i+=1


for link in links:

    driver.get(link)
    
    time.sleep(8)

    pyautogui.moveTo(100, 200)
    
    pyautogui.click(1751, 139) 
    pyautogui.click(803, 505)

    time.sleep(3)


