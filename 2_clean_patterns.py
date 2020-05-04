#encoding: utf-8

def apply(product, discount):
    price = int(product[1] * (1.0 - discount))
    assert price > 0
    return price

def discountPrice():
    product = [
        'pan',
        100,
        'tokyo',
    ]
    print(apply(product, 0.25))

discountPrice()

def withContext():
    with open('README.md') as f:
        for line in f:
            print(line)

withContext()

class Indenter:
    def __init__(self):
        self.level = 0
    def __enter__(self):
        self.level += 1
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1
    def print(self, text):
        print('  '*self.level + text)

def indentText():
    print('0')
    with Indenter() as i:
        i.print('a')
        with i:
            i.print('bb')
            with i:
                i.print('ccc')
            with i:
                i.print('ddd')
        i.print('e')
        with i:
            i.print('ff')
        i.print('g')

indentText()

class Test():
    def __init__(self):
        self.foo = 1
        self._bar = 2
        self.__hoge = 3
        self.__fuga__ = 4
        self._ = 5

def testUnderbar():
    print(Test().foo)
    print(Test()._bar)
    #print(Test().__hoge)
    print(dir(Test()))
    print(Test()._Test__hoge)
    print(Test().__fuga__)
    print(Test()._)

testUnderbar()

def formatStrings():
    name = 'hoge'
    print(f'my name is {name}')

formatStrings()
