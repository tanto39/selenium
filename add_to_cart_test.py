from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config import BASE_URL

# Тест добавления товара в корзину
def add_to_cart_test():
    # Настройка WebDriver (используем Chrome)
    driver = webdriver.Chrome()

    try:
        # Открываем сайт
        driver.get(BASE_URL)
        
        # Получаем первый товарный блок
        first_product = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-thumb"))
        )

        # Находим кнопку добавления в корзину (первая кнопка в этом блоке) и нажимаем
        add_to_cart_button = first_product.find_element(By.CSS_SELECTOR, 'button')
        actions = ActionChains(driver)
        actions.move_to_element(add_to_cart_button).click(add_to_cart_button).perform()

        print("Кнопка добавления в корзину нажата")
        
        # Ожидаем появления уведомления о добавлении в корзину
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
        )

        print("Уведомление получено")
        
        # Проверяем, что в корзине есть товар
        header_cart = driver.find_element(By.ID, "header-cart")
        cart_button = header_cart.find_element(By.CSS_SELECTOR, 'button')
        assert "1 item(s)" in cart_button.text, "Товар не добавлен в корзину"
        
        print("Тест пройден успешно, товар добавлен в корзину!")

    finally:
        # Закрываем браузер
        driver.quit()


add_to_cart_test()