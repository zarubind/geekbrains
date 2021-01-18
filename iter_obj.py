class Animal:
    def __init__(self, name):
        self.name = name

    def __iter__(self):
        for i in range(10):
            yield f'{self.name} делает {i}'

boris = Animal('Борис')

#for s in boris:
#    print(s)

boris = iter(boris)
while True:
    try:
        s = next(boris)
        print(s)
    except StopIteration:
        break
