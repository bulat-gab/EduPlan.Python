handlers = {}

class CustomMetaclass(type):
    def __new__(meta, name, bases, attrs):
        cls = type.__new__(meta, name, bases, attrs)
        for ext in attrs["formats"]:
            print(ext)
            handlers[ext] = cls
        return cls

class Handler(metaclass=CustomMetaclass):
    formats = "txt",

class ImageHandler(Handler):
    formats = "jpeg", "png"

class AudioHandler(Handler):
    formats = "mp3", "wav"

# h = Handler()
# i = ImageHandler()
# a = AudioHandler()

print(handlers)
