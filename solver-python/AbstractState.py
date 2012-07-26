class AbstractState(object):
    """Abstract class for problems being solved"""
    parent = None

    def __str__(self):
        raise NotImplementedError

    def getHashmapKey(self):
        raise NotImplementedError

    def getNext(self):
        raise NotImplementedError

    def getScore(self):
        raise NotImplementedError

    def isValid(self):
        raise NotImplementedError

    """TODO: private fields"""
    def g(self):
        raise NotImplementedError

    def h(self):
        raise NotImplementedError

    def parseString(self, input):
        raise NotImplementedError

    score = None
    hashmapKey = None