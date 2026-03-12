# Program 14: Check Pangram

def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    for letter in alphabet:
        if letter not in s:
            return False
    return True

sentence = "The quick brown fox jumps over the lazy dog"

print("Is pangram?", is_pangram(sentence))