import pkg_resources
import re

result = []


# 123

def get_dependencies(package_name):
    package = pkg_resources.working_set.by_key[package_name]
    for r in package.requires():
        print(r)
        r = "".join(c for c in str(r) if (c.isalpha() or c == '-' or c == '_'))
        result.append(package_name + " -> " + str(r))
        get_dependencies(r)

# а в пандас в одном имени пакеты указано сразу два пакета, найс, люблю эту штуку
get_dependencies("matplotlib")
print(result)
