#45. Maximum frequency character

s = input("Enter string: ")

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

max_char = max(freq, key=freq.get)
print("Maximum frequency character:", max_char)