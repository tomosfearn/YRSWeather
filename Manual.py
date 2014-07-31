import WindowControl

while True:
	input = raw_input("Open/Close: ")
	if input == "open":
		WindowControl.Open()
	else:
		WindowControl.Close()
