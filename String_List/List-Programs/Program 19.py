#19. Remove elements at even indices

lst = list(map(int, input("Enter list elements: ").split()))

result = []
for i in range(len(lst)):
    if i % 2 != 0:
        result.append(lst[i])

print("After removing even indices:", result)