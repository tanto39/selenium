from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config import BASE_URL

# Тест перехода на детальную страницу товара
def go_to_product_detail_test():
    driver = webdriver.Chrome()

    try:
        # Открываем главную страницу
        driver.get(BASE_URL)

        # Находим первый товар на странице
        first_product = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-thumb"))
        )

        # Находим и кликаем ссылку для перехода на детальную страницу товара
        product_link = first_product.find_element(By.CSS_SELECTOR, 'h4 a')
        product_name = product_link.text
        actions = ActionChains(driver)
        actions.move_to_element(product_link).click(product_link).perform()

        print("Ссылка перехода на детальную страницу товара нажата")

        # Ожидаем загрузки детальной страницы товара
        product_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )

        # Проверяем, что заголовок страницы соответствует названию товара
        assert product_name in product_title.text, "Название товара не совпадает"

        print("Тест пройден успешно, переход на детальную страницу выполнен корректно!")

    finally:
        driver.quit()


go_to_product_detail_test()
