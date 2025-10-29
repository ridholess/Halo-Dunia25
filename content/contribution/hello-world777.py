class MetaHello(type):
    def __new__(cls, name, bases, dct):
        dct['say_hello'] = lambda self: print("Hello, World!")
        return super().__new__(cls, name, bases, dct)

class Hello(metaclass=MetaHello):
    pass

def main_decorator(func):
    def wrapper():
        print("Initializing Hello World System...")
        func()
        print("Execution Complete ✅")
    return wrapper

@main_decorator
def main():
    h = Hello()
    h.say_hello()

if __name__ == "__main__":
    main()
