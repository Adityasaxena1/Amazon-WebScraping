from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Product_Details import find

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1')


def iterate():
    links = driver.find_elements(By.CSS_SELECTOR, '[class="a-link-normal s-underline-text s-underline-link-text s-link-'
                                                  'style a-text-normal"]')

    for link in links:
        driver.maximize_window()
        try:
            link.click()
        except:
            driver.find_element(By.CSS_SELECTOR,
                                '[class="a-link-normal a-carousel-goto-nextpage s-carousel-button"]').click()
            time.sleep(1)
            link.click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        find(dive=driver)
        driver.close()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])


iterate()
for _ in range(10):
    try:
        driver.find_element(By.CSS_SELECTOR, '[class="s-pagination-item s-pagination-next s-pagination-button '
                                             's-pagination-separator"]').click()
        time.sleep(2)
        iterate()
    except:
        pass

driver.close()
