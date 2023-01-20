C= input("Enter а temperature in degrees F: ")

def convert_cel_to_far(C):
    F = C * 9/5 + 32
    return F
b=f'{C}degrees F = {convert_cel_to_far(C)} degrees C'
print(b)


