import requests
import warnings
import threading
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# pip freeze > requirements.txt

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://dreampuf.github.io/GraphvizOnline/#digraph%20G%20%7B%0A%20%20%20%20%0A%7D")
graph_keys = driver.find_element_by_xpath('/html/body/pre/textarea')

warnings.filterwarnings('ignore')
passed = []


# level - на какое количество уровней вниз будет спускаться программа (x)
# iteration - какое количество зависимостей одной библиотеки будет выведено (x-1)
def get_dependencies(package_name, level):
    iteration = 0
    level += 1
    # Основа программы, достаёт json из pypi
    package_json = requests.get('https://pypi.org/pypi/{0}/json'.format(package_name), verify=False).json()
    packages = package_json['info']['requires_dist']
    if packages and (package_name not in passed):
        passed.append(package_name)
        for r in packages:
            # Проверка на каком уровне и сколько зависимостей
            if level >= 1 or iteration >= 8:
                break
            iteration += 1
            # Обрезаем версии библиотек и другие каракули
            del_char = [' ', '[', '<', '>', '=', ';', '~', '!']
            for repl in del_char:
                r = r.partition('{0}'.format(repl))[0]

            graph_keys.send_keys('"{0}" -> "{1}"\n'.format(package_name, r))
            get_dependencies(r, level)
        print(package_name, " finished;")


get_dependencies("pandas", 0 - 1)
i = input("Для продолжение нажмите любую клавишу...\n")
driver.quit()
# result = "digraph dependencies {\n" + get_dependencies("pandas") + "\n}"
