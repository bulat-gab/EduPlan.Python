class Base:
    pass

person1 = {
    "name" : "John",
    "age" : 37
}

person2 = {
    "name" : "A"
}

_person3_private = {
    "name" : "private person"
}

# __all__ = ["person1"]

if __name__ == "__main__":
    print("you are running base1 module as a script")
    print("Person2 is ", person2)
