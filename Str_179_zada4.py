try:
    user = int(input('vvedite integ number: '))
except ValueError:
    print("That was not ап integer")
else:
    print(user)