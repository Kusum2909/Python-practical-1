

# Create a sample input file
with open("input.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Python Programming\n")
    f.write("Hello Python\n")

# Read the file
with open("input.txt", "r") as f:
    content = f.read()

# (a) Count characters, words and lines
characters = len(content)
words = len(content.split())
lines = len(content.splitlines())

print("Total characters:", characters)
print("Total words:", words)
print("Total lines:", lines)

# (b) Frequency of each character
frequency = {}

for ch in content:
    frequency[ch] = frequency.get(ch, 0) + 1

print("\nCharacter frequency:")
print(frequency)

# (c) Print words in reverse order
word_list = content.split()

print("\nWords in reverse order:")
print(" ".join(word_list[::-1]))

# (d) Copy even lines to File1 and odd lines to File2
line_list = content.splitlines()

with open("File1", "w") as f1, open("File2", "w") as f2:
    for line_number, line in enumerate(line_list, start=1):
        if line_number % 2 == 0:
            f1.write(line + "\n")
        else:
            f2.write(line + "\n")

print("\nEven lines copied to File1.")
print("Odd lines copied to File2.")
