from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config import BASE_URL

# Тест добавления товара в сравнение
def test_add_to_compare():
    # Настройка WebDriver (используем Chrome)
    driver = webdriver.Chrome()

    try:
        # Открываем сайт
        driver.get(BASE_URL)

        # Получаем первый товарный блок
        first_product = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-thumb"))
        )

        # Ищем кнопку добавления в сравнение (третья кнопка в блоке) и кликаем по ней
        compare_button = first_product.find_elements(By.CSS_SELECTOR, "button")[2]
        actions = ActionChains(driver)
        actions.move_to_element(compare_button).click(compare_button).perform()

        print("Кнопка Compare нажата!")

        # Ожидаем появления уведомления
        alert = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
        )
        assert "Success" in alert.text, "Товар не добавлен в список сравнения!"
        print("Тест пройден успешно, товар добавлен в список сравнения!")

    finally:
        driver.quit()


test_add_to_compare()