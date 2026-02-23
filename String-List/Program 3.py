#3. Print words with their length

s = input("Enter string: ")
for w in s.split():
    print(w, ":", len(w))