
def prompt_values():
	return (int(input("Enter the first integer: ")), int(input("Enter the second integer: ")))

a,b = prompt_values()

print("""
Would you like to add or subtract your numbers?
a. Add
s. Subtract
m. Multiply
d. Divide
""")
val = input()
if val == "a":
	print(a + b)
elif val == "b":
	print(a - b)
elif val == "m":
	print(a * b)
elif val == "d":
	print(a / b)
