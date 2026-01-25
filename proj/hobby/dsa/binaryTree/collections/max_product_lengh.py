from collections import defaultdict
from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:

        chars = [set() for _ in range(26)]
        blocked = defaultdict(set)

        for i, word in enumerate(words):
            for c in word:
                idx = ord(c) - ord('a')
                chars[idx].add(i)

        for i, word in enumerate(words):
            for c in word:
                idx = ord(c) - ord('a')
                blocked[i].update(chars[idx])

        max_len = 0
        for k in blocked:
            all_indexes = {x for x in  range(len(words))}
            allowed = all_indexes.difference(blocked[k])
            for idx in allowed:
                max_len = max(max_len, len(words[k]) * len(words[idx]))

        return max_len