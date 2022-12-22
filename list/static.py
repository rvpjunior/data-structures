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
        if position > self.elements_counter:
            raise Exception("Empty house")

        return self.list[position]

    def remove(self, element):
        for array_item in self.list:
            if array_item = 
        pass

    def search(self, element):

        counter = 0
        found = 0
        found_elements = [None]*self.list_size
        for array_element in self.list:
            if array_element = element:
                found_elements[found] = counter
                found += 1
            counter += 1
        
        if found = 0:
            return f"{element} not found in list."
        
        counter = 0
        found_list = [None] * found
        for array_element in found_elements:
            if array_element is None:
                break
            found_list[counter] = found_elements[counter]
            counter += 1
        
        return print(f"{element} found in positions {found_list}.")            

    def __len__(self):
        return 0

    def __str__(self):
        return "List"