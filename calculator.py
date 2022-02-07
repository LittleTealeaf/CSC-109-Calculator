
def prompt_values():
	return (float(input("Enter the first number: ")), float(input("Enter the second number: ")))

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
	if b == 0:
		print("Error: Divide by 0")
	else:
		print(a / b)
