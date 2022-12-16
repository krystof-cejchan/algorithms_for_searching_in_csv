# pokud se x našlo, tak se vrátí jeho index
# pokud ne, tak se vrátí -1
def linear_search(arr, end, x, full_match):
    for i in range(0, end):
        if not full_match:
            if x in arr[i]:
                return i
        else:
            if arr[i] == x:
                return i
    return -1


# Rabin-Karp algorithm in python
def rabin_karp(searched, full_text, q):
    d = 10
    m = len(searched)
    n = len(full_text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(searched[i])) % q
        t = (d * t + ord(full_text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if full_text[i + j] != searched[j]:
                    break

            j += 1
            if j == m:
                return True

        if i < n - m:
            t = (d * (t - ord(full_text[i]) * h) + ord(full_text[i + m])) % q

            if t < 0:
                t = t + q

    return False


# knuth morris pratt
def kmp_search(pat, txt):
    M = len(pat)
    N = len(txt)

    lps = [0] * M
    j = 0

    compute_longest_previous_suffix_array(pat, M, lps)

    i = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            #   j = lps[j - 1]
            return True

        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False


def compute_longest_previous_suffix_array(pat, M, lps):
    length = 0

    i = 1

    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]

            else:
                lps[i] = 0
                i += 1
