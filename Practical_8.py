
# Create a list of cubes of even integers using for loop

items = eval(input("Enter a list: "))
cubes = []

for x in items:
    if isinstance(x, int) and not isinstance(x, bool) and x % 2 == 0:
        cubes.append(x ** 3)

print("Cubes of even integers:", cubes)
