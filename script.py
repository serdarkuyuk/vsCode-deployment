import math
import os
import sys

import requests


# name = input("your name")
# print("Hello ", name)

print(sys.version)
print(sys.executable)


def greet(who_to_great):
    greeting = "Hello, {}".format(who_to_great)
    return greeting


print(greet("World"))
print(greet("Serdar"))
r = requests.get("https://serdarkuyuk.netlify.app")
print(r.status_code)
