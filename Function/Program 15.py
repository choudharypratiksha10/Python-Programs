# Program 15: Sort Hyphen-Separated Words

def sort_words(s):
    words = s.split("-")
    words.sort()
    return "-".join(words)

items = "green-red-yellow-black-white"

print("Sorted sequence:", sort_words(items))