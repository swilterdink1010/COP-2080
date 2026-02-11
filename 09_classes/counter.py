class Counter:
    def __init__(self):
        self._value = 0
        self._string = ""
        self._limit = 0

    def getValue(self):
        return self._value
    
    def getString(self):
        return self._string
    
    def setLimit(self, limit):
        self._limit = limit

    def click(self):
        if (self._value == self._limit):
            print("Limit Reached")
            return        
        self._value += 1
        self._string += "|"
    
    def reset(self):
        self._value = 0