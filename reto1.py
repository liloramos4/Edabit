def longest_substring(digit_string):
    max_len = 0
    max_substr = ""
    curr_substr = ""
    for i in range(len(digit_string) - 1):
        if int(digit_string[i]) % 2 != int(digit_string[i+1]) % 2:
            curr_substr += digit_string[i]
        else:
            curr_substr += digit_string[i]
            if len(curr_substr) > max_len:
                max_len = len(curr_substr)
                max_substr = curr_substr
            curr_substr = ""
    curr_substr += digit_string[-1]
    if len(curr_substr) > max_len:
        max_substr = curr_substr
    return max_substr
