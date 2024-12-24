class vector:
    def __init__(self, r, e, d):
        self.r = r
        self.e = e
        self.d = d

    def get_values(self):
        return self.r, self.e, self.d
    def getR(self):
        return self.r
    def getE(self):
        return self.e
    def getD(self):
        return self.d
    def set_values(self, r=None, e=None, d=None):
        if r is not None:
            self.r = r
        if e is not None:
            self.e = e
        if e is not None:
            self.e = e
    def setR(self, r):
            self.r=r
    def setE(self, e):
            self.e=e
    def setD(self, d):
            self.d=d
    
    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index == 0:
            self._index += 1
            return self.r
        elif self._index == 1:
            self._index += 1
            return self.e
        elif self._index == 2:
            self._index += 1
            return self.d
        else:
            raise StopIteration
    def __repr__(self):
        return f"vector(arrival={self.r}, e={self.e}, d={self.d})"