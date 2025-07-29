class Solution:
    def asciirange(self, s: str):
        first_pos = {}
        last_pos = {}

        for i, ch in enumerate(s):
            if ch not in first_pos:
                first_pos[ch] = i
            last_pos[ch] = i

        result = []

        for ch in first_pos:
            start = first_pos[ch]
            end = last_pos[ch]
            if start != end:
                total = sum(ord(s[i]) for i in range(start + 1, end))
                if total > 0:
                    result.append(total)

        return result
