# def hello():
#     return "Hello world"
import functools

def decorate(func):
    def wrap(arg):
       print("I am before decorator")
       print(func(arg))
       print("I am a after decorator")
    return wrap

@decorate
def hello(name):
    return f"Hello {name}"

hello = decorate(hello)
hello()

