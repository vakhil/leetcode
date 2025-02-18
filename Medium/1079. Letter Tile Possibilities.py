from collections import defaultdict

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        arr_map = {}  
        char_freq = defaultdict(int)

        # Count frequency of characters
        for x in tiles:
            char_freq[x] += 1 

        def backtrack(current_str, count_freq):
            if current_str:
                arr_map[current_str] = 1  # Store unique sequence

            # Try adding each character if available
            for i in count_freq:
                if count_freq[i] > 0:
                    count_freq[i] -= 1  
                    backtrack(current_str + i, count_freq)
                    count_freq[i] += 1  # Backtrack

        backtrack("", char_freq.copy())  # Start recursion
        return len(arr_map)
