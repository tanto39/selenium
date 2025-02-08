from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config import BASE_URL
import random
import string

# Тест регистрации на сайте
def register_test():
    driver = webdriver.Chrome()
    
    try:
        driver.get(BASE_URL + "en-gb?route=account/register")
        
        # Заполняем поля регистрации
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "input-firstname"))
        ).send_keys("Test")
        
        driver.find_element(By.ID, "input-lastname").send_keys("User")
        
        email = "testuser" + "".join(random.choices(string.digits, k=5)) + "@example.com"
        driver.find_element(By.ID, "input-email").send_keys(email)
        
        driver.find_element(By.ID, "input-password").send_keys("Test@1234")

        print("Поля регистрации заполнены")

        # Получаем обертывающий блок и прокручиваем до него
        submit_wrapper = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-end")))
        actions = ActionChains(driver)
        actions.move_to_element(submit_wrapper).perform()
        
        # Ставим галочку согласия с политикой
        privacy_policy_checkbox = submit_wrapper.find_element(By.NAME, "agree")
        if not privacy_policy_checkbox.is_selected():
            privacy_policy_checkbox.click()

        print("Согласие с политикой проставлено")
        
        # Получаем кнопку отправки в блоке и нажимаем её
        submit_button = submit_wrapper.find_element(By.CSS_SELECTOR, "button")
        submit_button.click()

        print("Кнопка регистрации нажата")
        
        # Ожидаем появления подтверждающего сообщения
        # Ожидаем появления подтверждающего сообщения
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Your Account Has Been Created!')]")
        ))
        
        assert success_message is not None, "Сообщение о создании аккаунта не найдено!"
        
        print("Тест регистрации пройден успешно!")
    
    finally:
        driver.quit()


register_test()
