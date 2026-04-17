import re
def anagram(s1, s2):
    return sorted(re.sub(r'[^a-zA-Z]', '', s1).lower()) == sorted(re.sub(r'[^a-zA-Z]', '', s2).lower())

print(anagram("mata", "atma"))
print(anagram("mata", "tama"))
print(anagram("mata", "taam"))
print(anagram("mata", "makan"))
