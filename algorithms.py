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
    j = 0

    for i in range(m - 1):
        h = (h * d) % q
    try:
        for i in range(m):
            p = (d * p + ord(searched[i])) % q
            t = (d * t + ord(full_text[i])) % q
    except IndexError:
        # vyhledávaný text je delší než text ve kterém se hledá
        pass

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


# boyer moore algorithm
def bad_char_heuristic(string, size):
    NO_OF_CHARS = 256
    badChar = [-1] * NO_OF_CHARS

    for i in range(size):
        badChar[ord(string[i])] = i

    return badChar


def boyer_moore(txt, pat):
    m = len(pat)
    n = len(txt)

    badChar = bad_char_heuristic(pat, m)

    s = 0
    while s <= n - m:
        j = m - 1

        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1

        if j < 0:
            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
            return True
        else:
            s += max(1, j - badChar[ord(txt[s + j])])

    return False
