from Frame import Frame

class BowlingGame:
        score = 0
        rolls = 0
        frameList = [Frame]

        def Roll(pins):
            rolls += 1
            if (rolls % 2 ==0):
                frameList[-1].secondRoll = pins
        
        def IsPreviousFrameStrike():
            if (len(frameList) < 2):
                print("test")