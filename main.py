from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from db import MongoDriver

consulta = "zapatos"
driver = webdriver.Chrome()
driver.get("https://www.nike.com/us/es/")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="#VisualSearchInput")

search_box.send_keys(consulta)

search_button = driver.find_element(by=By.CSS_SELECTOR, value="#gen-nav-commerce-header-v2 > div.pre-l-header-container > header > div > div.pre-l-wrapper.mauto-sm.d-sm-flx > div.pre-l-nav-box.flx-gro-sm-1 > div > div > div.d-sm-flx.flx-jc-lg-fe.u-position-rel > div > div > button.pre-search-btn.ripple")
search_button.click()

shoes = driver.find_elements(By.CSS_SELECTOR, "#skip-to-products >div")

mongodb = MongoDriver()

for card in shoes:
   try:
        title = card.find_element(By.CSS_SELECTOR, "div > figure > a.product-card__link-overlay").text
        subtitle = card.find_element(By.CSS_SELECTOR, "div > figure > div > div.product_msg_info > div.product-card__titles > div.product-card__subtitle").text
        color = card.find_element(By.CSS_SELECTOR, "div > figure > div > div.product-card__count-wrapper.show--all.false > div > button > div").text
        price = card.find_element(By.CSS_SELECTOR, "div > figure > div > div.product-card__animation_wrapper > div").text
        print(title)
        print(subtitle)
        print(color)
        print(f"{price}")
        shoes_actual = {
                  "title": title,
                  "subtitle": subtitle,
                  "color": color,
                  "price": price,
             }

        mongodb.insert_record(record=shoes_actual, username="zapatos")

        print("++++++++++++++++++++++++++++++++")
   except Exception as e:
        print(e)
        print("++++++++++++++++++++++++++++++++")


driver.close()