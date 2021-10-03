def solution(s):
    len_s = len(s)
    for part_size in range(1, len_s+1):
        if len_s % part_size:
            continue
        part_cnt = len_s / part_size
        if s == (s[:part_size] * part_cnt):
            return part_cnt
    return 0


print(solution("abcabcabcabc"))
print(solution("abccbaabccba"))
print(solution("abcdefghijkl"))
print(solution("aaaaaaaaaaaa"))
