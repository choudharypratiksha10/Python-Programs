# Program 19: Access Function Inside Function

def outer():
    def inner():
        return "Inner function called"
    return inner()

print(outer())