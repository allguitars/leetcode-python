
# Approach 1:
# 這個方法沒問題，但有些面試官可能會要求你不用內建的方法 isalnum()，
# 或是要求你不要另外用額外的記憶體 new_s。
# 而 new_s[::-1] 背後其實也因為新增了相反的 string，佔了額外的記憶體空間。
def is_palindrome1(s):
    new_s = ''
    for c in s:
        if c.isalnum():
            new_s += c.lower()
    return new_s == new_s[::-1]


s1 = 'A man, a plan, a canal: Panama'
s2 = 'race a car'
s3 = ' '

assert is_palindrome1(s1) == True
assert is_palindrome1(s2) == False
assert is_palindrome1(s1) == True


# Approach 2:
# 空間複雜度 O(1)，只使用固定的記憶體空間，不受資料大小影響。
# 並且用 ASCII 碼來判定該字元是否為 alphanumerical
def is_palindrome2(s):
    l = 0
    r = len(s) - 1

    while l < r:
        while not alpha_num(s[l]) and l < r:
            l += 1
        while not alpha_num(s[r]) and l < r:
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l, r = l + 1, r - 1

    return True


def alpha_num(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


assert is_palindrome2(s1) == True
assert is_palindrome2(s2) == False
assert is_palindrome2(s1) == True

print('Pass')
