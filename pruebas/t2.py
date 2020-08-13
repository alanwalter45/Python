import doctest


def calculo1(a):
    """>>> calculo1(10) 
True
    """
    assert a == 10
    return True


def calculo2(a):
    """>>> calculo2(100) 
True
    """
    assert a != 10
    return True


doctest.testmod()
