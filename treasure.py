import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    # Берём значение x из атрибута valuex у картинки-сундука
    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)

    # Вводим ответ в текстовое поле
    browser.find_element(By.ID, "answer").send_keys(y)

    # Отмечаем checkbox "I'm the robot"
    browser.find_element(By.ID, "robotCheckbox").click()

    # Выбираем radiobutton "Robots rule!"
    browser.find_element(By.ID, "robotsRule").click()

    # Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # успеваем скопировать код из alert
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файле