def make_kmp_table(pattern):
    m = len(pattern)
    border = [-1] * (m+1)
    i = 0
    j = -1
    while i < m:
        while j >= 0 and pattern[i] != pattern[j]:
            j = border[j]
        i += 1
        j += 1
        border[i] = j
    return border

def kmp_search(pattern, border, text):
    m = 0
    i = 0
    t_len = len(text)
    p_len = len(pattern)

    while m+i < t_len:
        if pattern[i] == text[m+i]:
            if i == p_len-1:
                return m
            i += 1
        else:
            if border[i] > -1:
                m = m + i - border[i]
                i = border[i]
            else:
                i = 0
                m += 1

    return -1