def b():
    print('b() starts')
    c()
    print('b() returns')

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def d():
    print('d() starts')
    print('d() returns')

def c():
    print('c() starts')
    print('c() returns')


a()
