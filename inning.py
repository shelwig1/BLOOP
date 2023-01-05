#simluate an inning
#pitcher's batting avg vs random number generator, if good check single double triple homerun
import random
import itertools
"""
A game has:
innings
outs
batting order
individual pitches
scores
all of these variables for two teams, in order to let us compare strategies against one another
"""
#lineup = [bat1, bat2, bat3]

#Make it take an array of pitcher objects
def pitchInning(lineup):
	index = 0
	atBat = lineup[index]
	strikes = 0
	outs = 0

	inning = 0 
	while inning < 9:
		if random.randrange(0,1000) > atBat.battingavg:
			#miss
			#increment strike by 1
			strikes += 1
			if strikes == 3:
				outs += 1
				if outs == 3:
					#cycle the next batter in
					inning += 1
		else:
			#hit
			#calculate what kind of hit it was
			#cycle the next batter in 
			pass



""""
How to cycle through the lineup
items = [1,2]

for element in  itertools.cycle(items):
	print(element)
"""