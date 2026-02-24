#15. Find range of a list
#(Range = largest − smallest)

lst = list(map(int, input("Enter numbers: ").split()))

largest = max(lst)
smallest = min(lst)

range_val = largest - smallest
print("Range of list:", range_val)