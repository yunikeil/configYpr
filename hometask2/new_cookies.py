import pickle
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_cookies():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://funpay.com/lots/745/trade')

    driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div[3]'
                                 '/div/div/div/form/div[2]/input[1]').send_keys(config["auth"]["username"])
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div[3]'
                                 '/div/div/div/form/div[2]/input[2]').send_keys(config["auth"]["password"])

    f0 = input("=>")
    print("auth on " + config["auth"]["username"])
    pickle.dump(driver.get_cookies(), open('cookies_', 'wb'))
    driver.quit()


def check_cookies():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                                "(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36")

    driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
    driver.get('https://funpay.com')

    for cookie in pickle.load(open('cookies_', 'rb')):
        driver.add_cookie(cookie)

    driver.get('https://funpay.com/lots/745/trade')
    driver.get_screenshot_as_file('check_upload().png')
    print("cookies is ok")
    f = input()
    driver.quit()


config = configparser.ConfigParser()
config.read("settings.ini")

f = int(input("1 - create_cookies()\n2 - check_cookies"))
if f == 1:
    create_cookies()
else:
    check_cookies()
