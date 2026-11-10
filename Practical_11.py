
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a. Print half values in two lines
mid = len(t1) // 2

print("First half:", t1[:mid])
print("Second half:", t1[mid:])

# b. Print another tuple containing even numbers
even = tuple(x for x in t1 if x % 2 == 0)
print("Even numbers:", even)

# c. Concatenate t2 with t1
t2 = (11, 13, 15)
t3 = t1 + t2
print("Concatenated tuple:", t3)

# d. Find maximum and minimum
print("Maximum value:", max(t3))
print("Minimum value:", min(t3))
