from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from config import BASE_URL

# Тест сортировки товаров
def sort_test():
    driver = webdriver.Chrome()
    
    try:
        driver.get(BASE_URL + 'en-gb/catalog/component/monitor')
        
        # Ожидаем загрузки выпадающего списка сортировки
        sort_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "input-sort"))
        )
        
        # Выбираем сортировку по убыванию цены
        select = Select(sort_dropdown)
        select.select_by_visible_text("Price (High > Low)")

        print("Сортировка по убыванию цены выбрана")
        
        # Ожидаем обновления списка товаров после сортировки
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-thumb"))
        )

        print("Список товаров обновлен")
        
        # Получаем список всех отображаемых товаров и их цен
        product_prices = driver.find_elements(By.CSS_SELECTOR, ".product-thumb .price")
        
        # Извлекаем числовые значения цен
        prices = []
        for price in product_prices:
            price_text = price.text.split('\n')[0].split(' ')[0].replace("$", "").replace(",", "")
            prices.append(float(price_text))
        
        # Проверяем, что цены отсортированы по убыванию
        assert prices == sorted(prices, reverse=True), "Товары не отсортированы по убыванию цены!"
        
        print("Тест успешно пройден: товары отсортированы по убыванию цены.")
    
    finally:
        driver.quit()


sort_test()
