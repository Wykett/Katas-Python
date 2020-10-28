class Frame:
	firstRoll = 0
	secondRoll = 0
	isSpare = firstRoll + secondRoll == 10 and firstRoll != 10
	isStrike = firstRoll = 10