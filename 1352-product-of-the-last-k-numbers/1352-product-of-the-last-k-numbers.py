# Editorial based solution
# Use prefix product

# Time Complexity: O(1)
# Space Complexity: O(N)
class ProductOfNumbers:

    def __init__(self):
        self.size = 0
        self.prefix_prod = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.size = 0
            self.prefix_prod = [1]
        else:
            self.prefix_prod.append(num * self.prefix_prod[-1])
            self.size += 1
        

    def getProduct(self, k: int) -> int:
        if self.size < k:
            # Somewhere, we've encountered a zero
            return 0
        else:
            return self.prefix_prod[self.size] // self.prefix_prod[self.size-k]

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)