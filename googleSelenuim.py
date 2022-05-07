from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def mission4():
    global url, elmentPath
    driver_google = webdriver.Chrome('./chromedriver')
    url = 'https://translate.google.co.il/'
    driver_google.get(url)
    elmentPath = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea'
    driver_google.find_element(By.XPATH, elmentPath).send_keys("שלום עולם")
    driver_google.close()


# mission 4
# mission4()


def mission5():
    global url, elmentPath
    driver_youtube = webdriver.Chrome('./chromedriver')
    url = 'https://www.youtube.com/'
    driver_youtube.get(url)
    elmentPath = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input'
    searchElement = driver_youtube.find_element(By.XPATH, elmentPath)
    searchElement.send_keys("אייל גולן")
    searchElement.submit()

mission5()
# mission 5
# mission5()


def mission6():
    global url, textElement
    driver_google_output = webdriver.Chrome('./chromedriver')
    url = 'https://translate.google.co.il/'
    driver_google_output.get(url)
    elment_path_input = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea'
    elment_input = driver_google_output.find_element(By.XPATH, elment_path_input)
    elment_input.send_keys("שלום עולם")
    # driver_google_.close()
    elment_path_output = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[7]/div/div[1]/span[1]/span/span'
    elment_output = driver_google_output.find_element(By.XPATH, elment_path_output)
    textElement = elment_output.text
    # driver_google_output.close()
    print(textElement)


# mission6()
# mission7

driver_facebook = webdriver.Chrome('./chromedriver')
url = 'https://www.facebook.com'
driver_facebook.get(url)
driver_facebook.find_element_by_id("email").send_keys("a@a.com")
driver_facebook.find_element_by_id("pass").send_keys("Aa123456")


# driver.find_element_by_id("email").send_keys("a@a.com")
# driver_facebook.(find_element_by_id("pass").send_keys("Aa123456")

