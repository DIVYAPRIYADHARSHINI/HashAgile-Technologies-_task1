def is_palin(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True
def longest_palindrome(s):
    n = len(s)
    max_len = 0
    start_index = 0
    
    for i in range(n):
        for j in range(i, n):
            if is_palin(s, i, j):
                current_len = j - i + 1
                if current_len > max_len:
                    max_len = current_len
                    start_index = i
                    
    return s[start_index:start_index + max_len]
input_string = "babad"
final= longest_palindrome(input_string)
print(f"Longest Palindromic Substring: {final}")
