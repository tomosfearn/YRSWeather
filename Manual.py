import WindowControl

while True:
	input = raw_input("Open/Close? ")
	if input.upper == "OPEN":
		WindowControl.Open()
	elif input.upper == "CLOSE":
		WindowControl.Close()
	else:
		print("ERROR!!")
