import java.util.ArrayList;
import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        return hashMapSolution(nums, target);
    }

    public int[] hashMapSolution(int[] nums, int target) {
        // Time Complexity: O(N)
        // Space Complexity: O(N)
        int n = nums.length;
        HashMap<Integer, Integer> hashmap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int current = nums[i];
            int complement = target - nums[i];
            if (hashmap.containsKey(complement)) {
                int comp_index = hashmap.get(complement);
                return new int[] {comp_index, i};
            }
            hashmap.put(current, i);
        }
        return new int[] {-1, -1};
    }

    public int[] bruteForce(int[] nums, int target) {
        // Time Complexity: O(N ** 2)
        // Space Complexity: O(1)
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }
        return new int[] {-1, -1};
    }
}