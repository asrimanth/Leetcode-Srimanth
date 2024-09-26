# Time Complexity: O(N*2^N)
# Space Complexity: O(N) - excluding result output list

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        # Need sorting - so that we have same numbers side-by-side
        candidates = sorted(candidates)
        def dfs(idx, curr_subset, curr_total):
            if curr_total == target:
                result.append(curr_subset.copy())
                return
            if idx >= len(candidates) or curr_total > target:
                return
            
            # Left sub tree: Consider current candidate
            curr_subset.append(candidates[idx])
            dfs(idx+1, curr_subset, curr_total + candidates[idx])

            # Right sub tree: Do NOT consider current candidate,
            # Do NOT consider previous identical candidates
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            curr_subset.pop()
            dfs(idx+1, curr_subset, curr_total)

        dfs(0, [], 0)
        return list(result)
