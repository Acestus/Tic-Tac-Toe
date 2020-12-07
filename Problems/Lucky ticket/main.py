# Save the input in this variable
ticket = [int(n) for n in input()]

# Add up the digits for each half
half1 = sum(ticket[0:3])
half2 = sum(ticket[3:6])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
