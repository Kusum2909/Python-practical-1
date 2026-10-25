#WRITE A PROGRAM THAT ACCEPTS THE CHARACTER AND PERFORM THE FOLLOWING:
(a) CHECK WHETHER CHARACTER IS ALPHABET, NUMERIC OR SPECIAL CHARACTER. 
(b) IF CHARACTER IS LETTER, PRINT WHETHER IT IS UPPERCASE OR LOWERCASE. 
(c) IF CHARACTER IS NUMERIC, PRINT IT'S NAME IN TEXT. 


ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter only one character.")

elif ch.isalpha():
    print("It is a letter.")

    if ch.isupper():
        print("It is an uppercase letter.")
    else:
        print("It is a lowercase letter.")

elif ch.isdigit():
    print("It is a numeric digit.")

    digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
              "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

    print("Digit in words:", digits[int(ch)])

else:
    print("It is a special character.")
