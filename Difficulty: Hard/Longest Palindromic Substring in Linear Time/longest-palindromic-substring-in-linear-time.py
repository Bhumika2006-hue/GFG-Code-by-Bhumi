def LongestPalindromeSubString(text):
    if not text:
        return ""

    # Preprocess the string: "aba" -> "^#a#b#a#$"
    # ^ and $ are unique boundaries to avoid bounds checking
    T = "#" + "#".join(text) + "#"
    n = len(T)
    P = [0] * n
    C = 0  # Center of the rightmost palindrome
    R = 0  # Right boundary of the rightmost palindrome

    max_len = 0
    center_index = 0

    for i in range(n):
        # Find the mirror of i relative to C
        i_mirror = 2 * C - i

        # If i is within the boundary R, inherit the value from its mirror
        if i < R:
            P[i] = min(R - i, P[i_mirror])

        # Attempt to expand around i
        try:
            while i + 1 + P[i] < n and i - 1 - P[i] >= 0 and T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
        except IndexError:
            pass

        # If the palindrome at i expands past R, update C and R
        if i + P[i] > R:
            C = i
            R = i + P[i]

        # Track the largest palindrome found
        if P[i] > max_len:
            max_len = P[i]
            center_index = i

    # Extract the original string characters
    start = (center_index - max_len) // 2
    return text[start : start + max_len]