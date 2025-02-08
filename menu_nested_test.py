from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config import BASE_URL

# Тест работы вложенного пункта меню
def menu_nested_test():
    driver = webdriver.Chrome()
    
    try:
        driver.get(BASE_URL)
        
        # Ожидаем загрузки меню и находим пункт Components
        components_menu_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Components"))
        )
        
        # Наводим курсор на Components, чтобы появилось вложенное меню
        actions = ActionChains(driver)
        actions.move_to_element(components_menu_item).perform()
        
        # Ожидаем появления вложенного пункта Monitors и кликаем по нему
        monitors = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Monitors"))
        )
        # actions.move_to_element(monitors).click().perform()
        monitors.click()
        
        print("Кнопка вложенного пункта меню Monitors нажата")
        
        # Получаем блок левого меню
        left_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "column-left"))
        )
        
        # Проверяем, что в этом блоке пункт Monitors имеет класс active
        active_menu_item = WebDriverWait(left_menu, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//a[contains(text(), 'Monitors') and contains(@class, 'active')]")
        ))
        
        assert active_menu_item, "Ошибка: Страница Monitors не открылась"
        
        print("Тест перехода в раздел Monitors пройден успешно!")

    finally:
        driver.quit()


menu_nested_test()
