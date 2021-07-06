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
    
    def __init__(self, start=100):
        """ Create a serial number with a given starting number (default: start = 100)
        """
        self.start = start
        self.next_num = start 
    
    def __repl__(self):
    
        return f"SerialGenerator<start = {self.start} current = {self.next_num}>" 

    def generate(self):
        """ updates the instance's current serial number and returns previous current """

        # Learn how to use yield
        # yield self.current
        # return next(self.current)
        self.next_num += 1
        return self.next_num - 1 
    
    def reset(self):
        """ Resets the serial to start number"""
        self.next_num = self.start