class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        used = [False] * 26
        stack = []

        for c in s:
            idx = ord(c) - ord('a')
            freq[idx] -= 1

            if used[idx]:
                continue

            while stack:
                top = stack[-1]
                top_idx = ord(top) - ord('a')
                if top > c and freq[top_idx] > 0:
                    used[top_idx] = False
                    stack.pop()
                else:
                    break

            stack.append(c)
            used[idx] = True

        return "".join(stack)