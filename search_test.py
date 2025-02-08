from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config import BASE_URL

# Тест поиска по сайту
def search_test():
    driver = webdriver.Chrome()
    
    try:
        # Открываем сайт
        driver.get(BASE_URL)
        
        # Ожидаем появления строки поиска и вводим запрос
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search"))
        )
        search_box.send_keys("MacBook")
        
        # Отправляем поиск нажатием клавиши Enter
        search_box.send_keys(Keys.RETURN)
        print("Поисковый запрос отправлен")
        
        # Ожидаем появления результатов поиска
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-thumb"))
        )
        
        # Проверяем, что найдены товары
        products = driver.find_elements(By.CLASS_NAME, "product-thumb")
        assert len(products) > 0, "Результаты поиска не найдены"
        
        print("Тест пройден успешно, результаты поиска отображаются!")
    
    finally:
        driver.quit()


search_test()
