from selenium.webdriver.common.by import By
import time


def find(dive):
    name = dive.find_element(By.ID, value='productTitle').text
    price = dive.find_element(By.CLASS_NAME, value='a-price-whole').text
    try:
        rating = dive.find_element(By.CSS_SELECTOR, '[class="a-popover-trigger a-declarative"] '
                                                    '[class="a-size-base a-color-base"]').text
        number_of_ratings = dive.find_element(By.ID, value='acrCustomerReviewText').text
    except:
        rating = "No Rating"
        number_of_ratings = "No Ratings"
    time.sleep(2)
    descriptions = [description.text for description in dive.find_elements(By.CSS_SELECTOR, '[class="a-list-item '
                                                                                                'a-size-base a-color-base"]')]

    time.sleep(2)
    with open('product.csv', mode='a', encoding='utf-8') as csv_file:
        csv_file.write(f"\n{name}, "
                       f"₹{price}, "
                       f"{rating} out of 5 stars, "
                       f"{number_of_ratings}, "
                       f"{descriptions}"
                       )
