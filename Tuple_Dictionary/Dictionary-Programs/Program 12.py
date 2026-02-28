#12. Map two lists into a dictionary

l1 = input("Enter first list elements: ").split()
l2 = input("Enter second list elements: ").split()

d = dict(zip(l1, l2))
print(d)