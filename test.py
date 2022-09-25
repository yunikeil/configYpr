import requests

package_json = requests.get('https://pypi.org/pypi/matplotlib/3.6.0/json', verify=False).json()
print(package_json['info']['requires_dist'])
