#28. Slice a tuple

t = tuple(input("Enter elements: ").split())
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
print(t[start:end])