class Solution:
    def match(self, wild: str, pattern: str) -> bool:
        s = pattern
        p = wild
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = -1
        s_tmp_idx = -1

        # Traverse the text
        while s_idx < s_len:
            # Match char or '?'
            if p_idx < p_len and (p[p_idx] == s[s_idx] or p[p_idx] == '?'):
                s_idx += 1
                p_idx += 1

            # Record position of '*'
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1  # assume '*' matches empty for now

            # Mismatch, but we had a previous '*'
            elif star_idx != -1:
                p_idx = star_idx + 1          # move pattern to char after '*'
                s_tmp_idx += 1                # let '*' match one more char
                s_idx = s_tmp_idx

            # Mismatch and no '*' to fall back to
            else:
                return False

        # Remaining pattern chars must all be '*'
        while p_idx < p_len and p[p_idx] == '*':
            p_idx += 1

        return p_idx == p_len
