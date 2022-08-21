class CustomMetaClass(type):
    def __init__(cls, name, bases, attrs):
        for name, value in attrs.items():
            print('{} :{}'.format(name, value))

class SomeClass(metaclass=CustomMetaClass):
    class_attribute = 'Some string'
    def __int__(self):
        object_attribute = 'abc'



c = SomeClass()

