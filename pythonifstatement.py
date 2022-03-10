# Pytathon if Stement

# if Statement

sandwich_order = "Ham Roll"

if sandwich_order == "Ham Roll":
	print("Price: $1.75")

# if else Statement

tab = 29.95

if tab > 20:
	print("This user has a tab over $20 that needs to be paid.")
else:
	print("This user's tab is below $20 that does not require immediate payment.")

# elif Statement

sandwich_order = "Bacon Roll"

if sandwich_order == "Ham Roll":
	print("Price: $1.75")
elif sandwich_order == "Cheese Roll":
	print("Price: $1.80")
elif sandwich_order == "Bacon Roll":
	print("Price: $2.10")
else:
	print("Price: $2.00")

# Nested if Statement

sandwich_order = "Other Filled Roll"

if sandwich_order != "Other Filled Roll":
	if sandwich_order == "Ham Roll":
	  print("Price: $1.75")
if sandwich_order == "Cheese Roll":
	print("Price: $1.80")
elif sandwich_order == "Bacon Roll":
	print("Price: $2.10")

else:
	print("Price: $2.00")