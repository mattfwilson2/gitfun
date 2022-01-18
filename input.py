name = input()
difficulty = input()
null = ""

def askName():
	print("Enter your name: ")
	if name == null:
		print("Hello Player 1.")
	else:
		print(f"Hello, {name}.")

askName(name)

def diff():
	print("Choose your difficulty: [1] Easy, [2] Hard")
	if difficulty == "1":
		print("Easy mode selected.")
	elif difficulty == "2":
		print("Hard mode selected.")
	else:
		print("You haven't selected a difficulty.")

diff(difficulty)
