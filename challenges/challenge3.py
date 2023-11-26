'''
Given a lowercase string that has alphabetic characters only and no spaces,
 return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".
We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.
'''
def solve(lowercaseString):
    vowels = "aeiou"
    consonant_substrings = []
    current_substring_value = 0
    
    # Looping through the passed in string 
    for char in lowercaseString:
        if char not in vowels:
            current_substring_value += ord(char) - ord("a") + 1
        else: 
            if current_substring_value > 0:
                consonant_substrings.append(current_substring_value)
                current_substring_value = 0

    # Check for the last substring in case the string ends with a consonant
    if current_substring_value > 0:
        consonant_substrings.append(current_substring_value)  

    return max(consonant_substrings, default=0)              
