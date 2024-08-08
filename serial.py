"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        self.start = start
        self.x = -1

    def __repr__(self):
        return f"<SerialGenerator start={self.start + self.x + 1} next={self.start + self.x + 2}>"

    def generate(self):
        self.x += 1
        return self.start + self.x
        
    def reset(self):
        self.x = -1


    


