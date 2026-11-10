
# Function to find all occurrences of a string

def find_occurrences(s1, s2):
    indexes = []
    start = 0

    while True:
        index = s1.find(s2, start)

        if index == -1:
            break

        indexes.append(index)
        start = index + 1

    if len(indexes) == 0:
        return -1

    return indexes


s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

result = find_occurrences(s1, s2)

print("Result:", result)
