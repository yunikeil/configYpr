import pkg_resources
import re

result = []


# 123

def get_dependencies(package_name):
    package = pkg_resources.working_set.by_key[package_name]
    for r in package.requires():
        r = "".join(c for c in str(r) if (c.isalpha() or c == '-'))
        result.append(package_name + " -> " + r)
        get_dependencies(r)


get_dependencies("matplotlib")
print(result)
