#Create a function called shareFair() that returns true/false if a given variable x can be fairly divided by a given variable y with no remainder
def shareFair(x,y):
    if x % y == 0:
        return True
    else:
        return False