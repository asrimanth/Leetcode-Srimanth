import java.util.HashMap;
class Solution {
    public int finalValueAfterOperations(String[] operations) {
        // Time Complexity: O(N)
        // Space Complexity: O(1)
        HashMap<String, Integer> mapping = new HashMap<>();
        mapping.put("++X", 1);
        mapping.put("X++", 1);
        mapping.put("--X", -1);
        mapping.put("X--", -1);

        int result = 0;
        int n = operations.length;
        for(int i=0; i<n; i++) {
            int value = mapping.get(operations[i]);
            result += value;
        }
        return result;
    }
}