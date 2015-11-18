def dpMakeChange(coinValueList,change):
	''' Given a list of coin values and a desired amount of change, find the least amount of coins necessary to make that value'''
	minCoins = [0] * (change + 1) #minCoins remembers the minimum amount of coins required to make each value 
	temp = [] #temp stores the coins we want to use -> coins whos values are less than or equal to the current cent
	for cent in range(change + 1): 
		count = cent
		for j in coinValueList: 
			if j <= cent: 
				temp.append(j)
		for x in temp: #for each coin in the list of coins we want to use
			if minCoins[cent - x] + 1 < count: #if there is already a min number of coins for this value
				count = minCoins[cent - x] + 1 #increase the count of coins needed to make this value by one
		minCoins[cent] = count #store the number of coins required to make cent value for lookup
	return minCoins[change]



print(dpMakeChange([1,5,10,25], 98)) 
print(dpMakeChange([1,5,10,25, 41], 98)) #-> 41 + 41 + 10 + 5 + 1 = 5 
