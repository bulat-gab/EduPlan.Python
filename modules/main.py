# import my_package
# print(dir(my_package.base1))

# from my_package import base1
# print(dir(base1))

# from my_package import base1
# print(base1._person3_private)

from my_package.base1 import *

print(person1)
print(person2) # error
# print(_person3_private)

import my_package
print(my_package.base1._person3_private)
