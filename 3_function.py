#encoding: utf-8

def yell(text):
    return text.upper() + '!'

print(yell('hello'))

def testFuncs():
    bark = yell
    funcs = [
        bark,
        str.lower,
        str.capitalize,
    ]
    for f in funcs:
        print(f, f('hey there'))

testFuncs()

def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)

def whisper(text):
    return text.lower() + '...'

greet(yell)
greet(whisper)

def get_speak_func(text, volume):
    def murmur():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return murmur

print(get_speak_func('Hello, World', 0.7)())

def testLambda():
    tuples = [
        (1, 'd'),
        (2, 'b'),
        (4, 'a'),
        (3, 'c'),
    ]
    print(tuples)
    print(sorted(tuples))
    print(sorted(tuples, key=lambda x: x[1]))

    print(sorted(range(-5, 6), key=lambda x: x*x))

testLambda()

def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def hello():
    return 'hello'

print(hello())

import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def bye():
    """return a goodbye."""
    return 'Goodbye!'

print(bye.__name__)
print(bye.__doc__)
print(bye())
