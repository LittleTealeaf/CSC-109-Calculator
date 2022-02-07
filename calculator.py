
def prompt_values():
	return (int(input("Enter the first integer: ")), int(input("Enter the second integer: ")))

a,b = prompt_values()

print("""
Would you like to add or subtract your numbers?
a. Add
s. Subtract
""")
val = input()
if val == "a":
	print(a + b)
elif val == "b":
	print(a - b)

