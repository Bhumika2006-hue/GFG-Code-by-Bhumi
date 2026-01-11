# Function to fill lps[] for given pattern pat[0..M-1]
def computeLPSArray(pat, M, lps):
    length = 0 # length of the previous longest prefix suffix
    lps[0] = 0 # lps[0] is always 0
    i = 1

    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # This is the tricky part. We skip checking characters
                # and fall back to the previous longest prefix suffix.
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

# Function to check if the pattern exists in the string or not
def KMP(pat, txt):
    M = len(pat)
    N = len(txt)

    # Create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0] * M

    # Preprocess the pattern
    computeLPSArray(pat, M, lps)

    i = 0 # index for txt[]
    j = 0 # index for pat[]
    
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            # Pattern found
            return True
        
        # Mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return False