def function(value):
    for k in value:
        print(k)


def functionargs(*args):
    for i in args:
        print(i)


def functionkwargs(*args, **kwargs):
    for j in kwargs.items():
        print(j)
