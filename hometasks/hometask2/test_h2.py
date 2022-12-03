import requests
import warnings

warnings.filterwarnings('ignore')
del_char = [' ', '[', '<', '>', '=', ';', '~', '!']
passed = []


def func1(package_name, level, per_a, per_b):
    iteration = 0
    level += 1
    package_json = requests.get('https://pypi.org/pypi/{0}/json'.format(package_name), verify=False).json()
    packages = package_json['info']['requires_dist']
    if packages and (package_name not in passed):
        passed.append(package_name)
        for package in packages:
            if level >= per_a or iteration >= per_b: break
            iteration += 1
            for letter in package:
                if letter in del_char:
                    package = package.split(letter)[0]
            print(f'"{package_name}"->"{package}"')
            func1(package, level, per_a, per_b)

# Проверка на каком уровне(per_a) и сколько зависимостей(per_b)
func1("pandas", 0 - 1, 2, 8)
####################################################################################
####################################################################################
import requests
import warnings

warnings.filterwarnings('ignore')
passed = []


def func1(package_name):
    package_json = requests.get('https://pypi.org/pypi/{0}/json'.format(package_name), verify=False).json()
    packages = package_json['info']['requires_dist']
    del_char = [' ', '[', '<', '>', '=', ';', '~', '!']
    if packages:
        for package in packages:
            if package not in passed:
                passed.append(packaWe)
                for letter in package:
                    if letter in del_char:
                        package = package.split(letter)[0]
                print(package_name+ "->" +package)
                func1(str(package))
func1("pandas")