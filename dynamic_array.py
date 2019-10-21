# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# KRISTEN ORUE 

class DynamicArray(object):

    def __init__(self):
    # body of the constructor
        self.array = []
        self.capacity = 10
        self.n = 0


    def is_empty(self):
        return self.array == []

    def __len__(self):
        return self.n

        

    