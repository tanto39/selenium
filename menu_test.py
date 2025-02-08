from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL

# Тест перехода в пункт меню
def menu_test():
    driver = webdriver.Chrome()
    
    try:
        driver.get(BASE_URL)
        
        # Ожидаем загрузки меню и находим пункт Tablets
        tablets_menu_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Tablets"))
        )
        
        # Кликаем по пункту меню Tablets
        tablets_menu_item.click()
        
        print("Кнопка меню Tablets нажата")
        
        # Проверяем, что открыта страница с планшетами
        header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Tablets')]")
        ))
        
        assert "Tablets" in header.text, "Ошибка: Страница Tablets не открылась"
        
        print("Тест перехода в раздел Tablets пройден успешно!")
    
    finally:
        driver.quit()


menu_test()
