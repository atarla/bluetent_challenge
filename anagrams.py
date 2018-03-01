def isAnagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()  # sort first string
    list_str2 = list(str2)
    list_str2.sort() # sort second string

    return (list_str1 == list_str2)


print(isAnagram('anagram', 'nagaram'))
print(isAnagram('cat', 'rat'))

# better way using hashmap
# to increment a count(occurance) of each letter in str1 and decrement count of that letter in str2. if hashmap=0 they are anagrams
