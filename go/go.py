# I made this poem with Python. The title is "Go". Go is a very simple program with only instruction "go".
# If user types "go", the Go will print "Good."
# If user types any other instruction except "go", then Go will print "We have to go."
# So user have to keep going like our lives.
def go(word):
	if word == "go":
		return "Good."
	else:
		return "We have to go."

while True:
	print go(raw_input())
