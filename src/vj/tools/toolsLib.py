'''
Created on May 18, 2012

@author: Vijay Ananth

'''

def containsAny(mystr, charset):
    """Check whether 'mystr' contains ANY of the chars in 'charset'"""
    return 1 in [c in mystr for c in charset]

def containsAll(mystr, charset):
    """Check whether 'mystr' contains ALL of the chars in 'charset'"""
    return 0 not in [c in mystr for c in charset]

def  containsOnlyFrom(mystr, charset):
    """Check whether 'mystr' contains ONLY chars in 'charset' """
    for c in mystr:
        if c in charset:
            #remove c from list
            charset=charset.replace(c, '', 1)
        else:
            return False   
    return True      


if __name__ == "__main__":
    #unit tests, must print "OK!" when run
    assert containsAny('*.py', '*?[]')
    assert not containsAny('file.txt', '*?[]')
    assert containsAll('43221', '123')
    assert not containsAll('134', '123')
    assert containsOnlyFrom('bird', 'dbiir')
    assert not containsOnlyFrom('birdi', 'dbir')
    print "Lib OK!"