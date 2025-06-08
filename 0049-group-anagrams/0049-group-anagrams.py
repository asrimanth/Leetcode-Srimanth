from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.group_by_sorted_str(strs)
    
    def group_by_sorted_str(self, strs: List[str]) -> List[List[str]]:
        # Time Complexity: O(N*K*log(K))
        # Space Complexity: O(N*K)
        data_struct = defaultdict(list)
        for data in strs:
            data_struct[tuple(sorted(data))].append(data)
        return list(data_struct.values())
