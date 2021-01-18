import time

# Пример использования, передавать в upper_decorator(retry=5) и выполнять это число раз какую-то функцию, если
# предыдущее выполнение было неуспешным (передавать пакет по ip несколько раз, пока не передастся и т.п.)

def upper_decorator(name):
    def decorator(func):
        print(name)
        def wrapped():
            print('Я начинаюсь!')
            func()
            print('Я заканчиваюсь!')
        return(wrapped)
    return decorator

@upper_decorator(name='Privet')
def work():
    time.sleep(1)
    print('Я исходная функция')

work()

#import time
#
#def decorator(func):
#    def wrapped():
#        print('Я начинаюсь!')
#        func()
#        print('Я заканчиваюсь!')
#    return(wrapped)
#
#@decorator
#def work():
#    time.sleep(1)
#    print('Я исходная функция')
#
#work()
