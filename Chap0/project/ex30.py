people = 30
cars = 40
buses = 15

if cars > people:
	print ("We should take the cars.")
elif cars < people:
	print ("We should not take the cars.")
else:
	print ("We can't decided.")

if buses > cars:
	print ("That's too many buses.")
elif buses < cars:
	print ("Maybe we should take the buses.")
else:
	print ("We still can't decides.")

if people > buses:
	print ("Alright, let's take the buses.")
else:
	print ("Let's stay home then.")

