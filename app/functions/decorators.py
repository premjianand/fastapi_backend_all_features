def decorator1(func):
    def wraper():
        print( 'Hi, This is from decorator - 1 before execution.')
        func
        print( 'Hi, This is from decorator - 1 after execution.')
    return wraper

def decorator2(func):
    def wraper():
        func
        return 'Hi, This is from decorator - 2.'
    return wraper