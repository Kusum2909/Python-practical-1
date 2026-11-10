
# Program to swap the first n characters of two strings

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
n = int(input("Enter the value of n: "))

new_s1 = s2[:n] + s1[n:]
new_s2 = s1[:n] + s2[n:]

print("First string after swapping:", new_s1)
print("Second string after swapping:", new_s2)
