class Parrot:
    def __init__(self):
        self._voltage = 10

    @property # getter
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, value):
        self._voltage = value if value < 100 else 100

    @voltage.deleter
    def voltage(self):
        print('Меня удалили')
        del self._voltage

a = Parrot()
print(a.voltage)
a.voltage = 9
print(a.voltage)
a.voltage = 1000
print(a.voltage)
del a.voltage
