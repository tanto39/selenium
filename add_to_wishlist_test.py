from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config import BASE_URL

# Тест добавления товара в WishList
def add_to_wishlist_test():
    # Настройка WebDriver (используем Chrome)
    driver = webdriver.Chrome()
    
    try:
        # Открываем сайт
        driver.get(BASE_URL)

        # Получаем первый товарный блок
        first_product = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-thumb"))
        )

        # Находим кнопку добавления в Wish List (это вторая кнопка) и нажимаем
        wishlist_button = first_product.find_elements(By.CSS_SELECTOR, "button")[1]
        actions = ActionChains(driver)
        actions.move_to_element(wishlist_button).click(wishlist_button).perform()
        
        print("Кнопка добавления в Wish List нажата")

        # Ожидаем появления уведомления об успехе
        success_alert = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
        )
        
        assert success_alert is not None, "Ошибка: уведомление не появилось!"
        print("Тест пройден успешно")

    finally:
        driver.quit()


add_to_wishlist_test()
