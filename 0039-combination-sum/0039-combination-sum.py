class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(idx, curr_subset, curr_total):
            if target == curr_total:
                result.append(curr_subset.copy())
                return
            if curr_total > target or idx >= len(candidates):
                return
            
            # Include candidates[idx] or not
            curr_subset.append(candidates[idx])
            dfs(idx, curr_subset, curr_total + candidates[idx])

            # Don't include the current cand => move on to next candidate
            curr_subset.pop()
            dfs(idx+1, curr_subset, curr_total)

        dfs(0, [], 0)
        return result
