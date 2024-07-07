class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles >= numExchange:
            full_bottles = numBottles // numExchange
            empty_bottles = numBottles % numExchange
            total += full_bottles
            numBottles = full_bottles + empty_bottles
        return total
