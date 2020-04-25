class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = {}
        

    def add(self, key: int) -> None:
        self.stack[key] = True

    def remove(self, key: int) -> None:
        if key in self.stack.keys():
            self.stack[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.stack.keys() and self.stack[key] == True:
            return True
        else:
            return False


