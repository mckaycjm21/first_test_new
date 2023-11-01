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
    def __init__(self, start=0):
        """Initializes the generator with 0 as the default for start."""

        self.start = self.next = start

    def __repr__(self):
        """Easier to read out of the values"""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Add one to current serial and return the sum"""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset to start."""

        self.next = self.start