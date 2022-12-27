resistors = [0.27, 0.33, 0.51, 1, 1.5, 2.2, 3.3,4.7, 5, 5.6, 7.5, 8.2, 10, 12.4, 12.7, 13.3, 15, 18.2, 20, 22.1, 24.9, 27.4, 30.1, 34.8, 36.5, 40.2,43.2, 47.5, 49.9, 56.2, 60.4, 75, 82.5, 86.6, 100, 121, 150, 174, 200, 221, 237, 249, 301, 332, 402, 453, 475, 499, 604, 649, 681, 750, 825, 1000, 1210, 1500, 1740, 2000, 2150, 2210, 2370, 2490, 2740, 3010, 3240,3480, 3650, 4020, 4120, 4320, 4530, 4750,4990, 5230,5360, 5490, 6040, 6810, 6980, 7500, 8060, 8250, 9090, 10000, 11000, 11800, 121000, 12700, 13000, 13300, 15000, 17400, 18200, 20000, 22100, 23700, 24900, 27400, 30100, 34800, 36500, 40200, 45300, 47500, 49900, 54900, 57600, 60400, 64900, 69800, 75000, 82500, 90900, 95300, 100000, 121000, 147000, 150000, 174000, 200000, 237000, 249000, 255000, 274000, 324000, 348000, 365000, 402000, 453000, 475000, 499000, 549000, 576000, 604000, 649000, 750000, 909000]

newfile = open("parallel.txt", 'w')
for R1 in resistors:
		for R2 in resistors:
			R = (1/R1) + (1/R2)
			R = (1/R)
			newfile.write('{}  {} {} \n'.format(round(R, 3), R1, R2))
			
newfile.close()
		