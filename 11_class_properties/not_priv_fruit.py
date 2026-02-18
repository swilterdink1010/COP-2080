# not_priv_fruit.py
class Fruit:
    def __init__(self, factor):
        self._factor = factor
    def op1(self):
        print('Op1 with factor {}...'.format(self._factor))
class Apple(Fruit): # subclass
    def op2(self, factor):
        self.__factor = factor
        print('Op2 with factor {}...'.format(self.__factor))
obj = Apple('red')
obj.op1()    # Op1 with factor red...
obj.op2('green')  # Op2 with factor green...
obj.op1()    # This should be red, but is

print(obj.__dict__.keys())