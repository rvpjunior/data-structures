class StaticList():

    elements_counter = 0

    def __init__(self, list_size):
        self.list_size = list_size
        self.list = [None]*list_size

    def insert(self, element):
        if self.elements_counter >= self.list_size:
            raise Exception("List out of bounds")
        
        self.list[self.elements_counter] = element
        self.elements_counter += 1

    def get(self, position):
        if position >self.elements_counter:
            raise Exception("Empty house")

        return self.list[position]

    def remove(self):
        pass

    def search(self):
        pass

    def __len__(self):
        return 0

    def __str__(self):
        return "List"