def isAnagram(str1, str2):
    string_match = {}

    for letter in str1:
        string_match[letter] = string_match.get(letter, 0) + 1  # increment letter counter
    for letter in str2:
        string_match[letter] = string_match.get(letter, 0) - 1  # decrement if letter fount in second string
    # print(string_match.values())
    if any(val != 0 for val in string_match.values()):  # Anagram if all letter counter are zero
        return "false"
    else:
        return "true"



print(isAnagram('anagram', 'nagaram'))
print(isAnagram('cat', 'rat'))
