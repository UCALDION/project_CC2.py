def is_vowel_sandwich(word):
    # Check if the word is exactly 3 characters long
    if len(word) != 3:
        return False
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'v', 'w', 'x', 'y', 'z'}

    if word[0] not in vowels and word[1] in vowels and word[2] not in vowels:
        return True
    else:
        return False

print(is_vowel_sandwich("gym"))
print(is_vowel_sandwich("day"))
print(is_vowel_sandwich("leg"))
print(is_vowel_sandwich("pull"))
print(is_vowel_sandwich("push"))
