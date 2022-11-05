import math

#planning to add classes
#to make kohm and mohm valued resistors
#more readable

#also planning to merge both modes
#so that when a value is queried 
#all possible combos are displayed

resistors = [0.27, 0.33, 0.51, 1, 1.5, 2.2, 3.3,4.7, 5, 5.6, 7.5, 8.2, 10, 12, 12.7, 15, 18.2, 20, 22.1, 24.9, 27.4, 30.1, 47.5, 49.9, 56.2, 60.4, 75, 82.5, 86.6, 100, 121, 150, 174, 200, 221, 237, 249, 301, 332, 402, 453, 475, 499, 604, 649, 681, 750, 825, 1000, 1210, 1500, 1740, 2000, 2150, 2210, 2370, 2490, 2740, 3010, 3240, 3480, 3650, 4020, 4120, 4320, 4530, 4750, 4990, 5230, 5360, 5490, 6040, 6810, 6980, 7500, 8060, 8250, 9090, 10000, 11000, 11800, 12100, 12700, 13000, 13300, 15000, 17400, 18200, 20000, 22100, 23700, 24900, 27400, 30100, 34800, 36500, 40200, 45300, 47500, 49900, 54900, 57600, 60400, 64900, 69800, 75000, 82500, 90900, 95300, 100000, 121000, 147000, 150000, 174000, 200000, 237000, 249000, 255000, 274000, 301000, 324000, 348000, 365000, 402000, 453000, 475000, 499000, 549000, 576000, 604000, 649000, 750000, 909000, 1000000, 1500000, 2000000]

parallelList = open("parallel.txt", 'r')

print("Type 'p' for parallel mode and 's' for series mode.")

run = True
mode = input(' ')

while run:
	R = float(input("Enter Resistance Needed: "))
	if mode == 'p':
	    if R in resistors:
	    	print(R)
	    else:
	    	diff = 999
	    	possible = []
	    	inexact = False
	    	
	    	for val in parallelList:
	    			rVal = val.split()
	    			if float(rVal[0]) == R:
	    				print("{}: {}, {}".format(rVal[0],rVal[1], rVal[2]))
	    				break
	    			elif float(rVal[0]) > R and float(rVal[0]) <= (R + 0.5):
	    				inexact = True
	    				tempDiff = float(rVal[0]) - R
	    				if tempDiff < diff:
	    					diff = tempDiff
	    					if len(possible) == 0:
	    						possible.append(rVal[0])
	    						possible.append(rVal[1])
	    						possible.append(rVal[2])
	    					else:
	    						possible[0] = rVal[0]
	    						possible[1] = rVal[1]
	    						possible[2] = rVal[2]
	    	if inexact:
	    		print("{}: {}, {}".format(possible[0], possible[1], possible[2]))
	  
	
	elif mode == 's':    			
		possible = 0
	
		if R in resistors:
			print(R)
		elif (R <= 999):
			if (R + 1) in resistors:
				print(R + 1)
			elif (R - 1) in resistors:
				print(R - 1)
			elif (R + 2) in resistors:
				print(R + 2)
			elif (R - 2) in resistors:
				print(R - 2)
			else:
				for n in resistors:
					nR = R - n
					nR = math.trunc(nR)
					if nR in resistors:
						print(nR, n)
						possible += 1
					elif (nR + 1) in resistors:
						print(nR + 1, n)
						possible += 1
					elif (nR - 1) in resistors:
						print(nR - 1, n)
						possible +=1
				if possible == 0:
					print("Resistors in parallel, use chart")

