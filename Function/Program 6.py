# Program 6: Check Whether Number Falls Within Given Range

def check_range(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False

number = int(input("Enter number: "))
start_range = int(input("Enter start of range: "))
end_range = int(input("Enter end of range: "))

print("Is number within range?", check_range(number, start_range, end_range))