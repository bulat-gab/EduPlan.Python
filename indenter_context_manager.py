class Indenter:
    def __init__(self):
        self.level = -4

    def __enter__(self):
        self.level += 4
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 4

    def print(self, str_input):
        print(" " * self.level, str_input, sep='')

with Indenter() as indent:
    indent.print("hi")
    with indent:
        indent.print("hello")
        with indent:
            indent.print("bonjour")
    indent.print("hey")
