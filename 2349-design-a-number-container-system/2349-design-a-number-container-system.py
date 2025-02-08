# class NumberContainers:

#     def __init__(self):
        

#     def change(self, index: int, number: int) -> None:
        

#     def find(self, number: int) -> int:
        
from collections import defaultdict
from sortedcontainers import SortedSet
class NumberContainers:

    def __init__(self):
        self.data = dict()
        self.inv_index = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index in self.data:
            old_num = self.data[index]
            if old_num in self.inv_index and index in self.inv_index[old_num]:
                self.inv_index[old_num].remove(index)
                if not self.inv_index[old_num]:
                    del self.inv_index[old_num]

        self.data[index] = number
        self.inv_index[number].add(index)


    def find(self, number: int) -> int:
        if number in self.inv_index and len(self.inv_index[number]):
            return self.inv_index[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)