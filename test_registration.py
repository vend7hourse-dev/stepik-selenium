from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
# Для проверки бага замените ссылку на:
# link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Уникальные селекторы: поля ищем внутри блока .first_block
    browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("ivan@test.com")

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Даём странице время загрузиться
    time.sleep(1)

    # Проверяем, что регистрация прошла успешно
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Пауза, чтобы визуально оценить результат
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла