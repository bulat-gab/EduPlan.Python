class MyContextManager:
    def __init__(self, name="World"):
        self.name = name

    def __enter__(self):
        print("Entering the context")
        return f"Hello, {self.name}!"

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context")
        if isinstance(exc_value, IndexError):
            print(f"An exception occured in your with block: {exc_type}")
            print(f"Exception message: {exc_value}")
            return True

        print(exc_type, exc_value, exc_tb, sep="\n")


with MyContextManager("Bulat") as hello:
    print(hello)
    hello[100]
    print("after the line throwing an exception")

print("Continue normally from here...")
