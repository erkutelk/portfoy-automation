import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class pom():
    def __init__(self, driver):
        self.driver = driver

    def text_giris_islemleri(self, css_selector, text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((css_selector))
            )
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f'Text girişi hatası: {e}')
            return False

    def tıklama(self, css_selector):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(css_selector)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)#Button aşağıda kalıyor o yüzden sayfayı aşağıya kaydırmak için kullanılıyor.
            time.sleep(0.5)  #Bekleme ekeldik
            element.click()
            return True
        except Exception as e:
            print(f'Tıklama hatası: {e}')
            return False


    def select_dropdown_by_value(self, name_attr, value):
        try:
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, name_attr))
            )
            select = Select(dropdown)
            select.select_by_value(value)
        except Exception as e:
            print(f'Dropdown hatası: {e}')

    def dosya_yukle(self, name_attr, dosya_yolu):
        try:
            upload_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, name_attr))
            )
            upload_input.send_keys(dosya_yolu)
            return True
        except Exception as e:
            print(f'Dosya yükleme hatası: {e}')
            return False

    def text_al(self, css_selector):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
            )
            text_dogru = element.text
            print(text_dogru)

            return "Blog Başarıyla Eklendi"
               
        except Exception as e:
            return 'Hata'