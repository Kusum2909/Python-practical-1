
try:
    name = input("Enter your name: ")

    if not name.replace(" ", "").isalpha():
        raise ValueError("Name should contain only alphabets")

    print("Valid name:", name)

except ValueError as e:
    print("Invalid input:", e)
