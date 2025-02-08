from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config import BASE_URL

EMAIL = "test@example.com"
PASSWORD = "test39"

# Тест входа на сайт
def login_test():
    driver = webdriver.Chrome()
    
    try:
        driver.get(BASE_URL + "en-gb?route=account/login")

        form_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#form-login"))
        )
        
        # Вводим email
        form_login.find_element(By.ID, "input-email").send_keys(EMAIL)
        
        # Вводим пароль
        form_login.find_element(By.ID, "input-password").send_keys(PASSWORD)
        
        print("Данные для входа введены")
        
        # Прокручиваем до кнопки входа и нажимаем её
        submit_button = form_login.find_element(By.CSS_SELECTOR, "button")
        actions = ActionChains(driver)
        actions.move_to_element(submit_button).click(submit_button).perform()

        print("Кнопка входа нажата")
        
        # Ожидаем перехода в аккаунт
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'My Account')]")
        ))
        
        assert success_message is not None, "Ошибка: вход в аккаунт не выполнен!"
        print("Тест входа пройден успешно!")
    
    finally:
        driver.quit()


login_test()
