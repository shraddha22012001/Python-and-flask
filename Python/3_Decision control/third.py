#Write a Python program to test whether a passed letter is a vowel or not.
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels

var = input('Enter a letter :')
if is_vowel(var):
    print("Letter "+ var +" is a Vowel")
else:
     print("Letter "+ var + " is not a Vowel")


