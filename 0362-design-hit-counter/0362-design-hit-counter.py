# Time Complexity: O(1) for hit, O(log(N)) for getHits
# Space Complexity: O(N)
class HitCounter:
    def __init__(self):
        self.timestamps = []
        self.count = 0

    def hit(self, timestamp: int) -> None:
        self.timestamps.append(timestamp)
        self.count += 1

    def getHits(self, timestamp: int) -> int:
        left = 0
        right = self.count - 1
        target = timestamp - 300
        while left <= right:
            mid = (left + right) // 2
            if self.timestamps[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        return self.count - left

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)