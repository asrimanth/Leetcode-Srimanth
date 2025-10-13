import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<String> removeAnagrams(String[] words) {
        // Time Complexity: O(N * K), N = len(words), K = len(each_word)
        // Space Complexity: O(N) for the result list
        if (words.length == 0) {
            return new ArrayList<>();
        }

        List<String> result = new ArrayList<>();
        result.add(words[0]); // Add the first word unconditionally

        for (int i = 1; i < words.length; i++) {
            String lastInResult = result.get(result.size() - 1);
            String curr = words[i];
            if (!areAnagramsHashMap2(lastInResult, curr)) {
                result.add(curr);
            }
        }

        return result;
    }

    public boolean areAnagramsHashMap2(String string1, String string2) {
        /**
        * Anagram Time Complexity: O(K)
        * Anagram Space Complexity: O(K)
        */
        if (string1.length() != string2.length()) {
            return false;
        }

        Map<Character, Integer> charCounts = new HashMap<>();

        // Increment counts for string1
        for (char c : string1.toCharArray()) {
            charCounts.put(c, charCounts.getOrDefault(c, 0) + 1);
        }

        // Decrement counts for string2
        for (char c : string2.toCharArray()) {
            Integer count = charCounts.get(c);
            if (count == null || count == 0) { // Character not found or already depleted
                return false;
            }
            charCounts.put(c, count - 1);
        }

        // Check if all counts are zero
        for (int count : charCounts.values()) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }

    /**
     * Anagram Time Complexity: O(K)
     * Anagram Space Complexity: O(K) + O(K) = O(K)
     */
    public boolean areAnagramsHashMap1(String string1, String string2) {
        if (string1.length() != string2.length()) {
            return false;
        }

        Map<Character, Integer> charCounts1 = new HashMap<>();
        Map<Character, Integer> charCounts2 = new HashMap<>();

        for (char c : string1.toCharArray()) {
            charCounts1.put(c, charCounts1.getOrDefault(c, 0) + 1);
        }
        for (char c : string2.toCharArray()) {
            charCounts2.put(c, charCounts2.getOrDefault(c, 0) + 1);
        }

        return charCounts1.equals(charCounts2);
    }

    
    public boolean areAnagramsSort(String string1, String string2) {
        /**
        * Anagram Time Complexity: O(K * log(K))
        * Anagram Space Complexity: O(K) + O(K) = O(K)
        */
        if (string1.length() != string2.length()) {
            return false;
        }

        char[] chars1 = string1.toCharArray();
        char[] chars2 = string2.toCharArray();

        Arrays.sort(chars1);
        Arrays.sort(chars2);

        return Arrays.equals(chars1, chars2);
    }
}