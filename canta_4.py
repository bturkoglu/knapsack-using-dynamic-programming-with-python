
def knapsack(items, maxweight):
	# Create an (N+1) by (W+1) 2-d list to contain the running values
	# which are to be filled by the dynamic programming routine.
	#
	# There are N+1 rows because we need to account for the possibility
	# of choosing from 0 up to and including N possible items.
	# There are W+1 columns because we need to account for possible
	# "running capacities" from 0 up to and including the maximum weight W.

	kolonlar = maxweight + 1
	satirlar = len(items) + 1
	bestvalues = [[0] * kolonlar for i in range(satirlar)]

	keep = [[0] * kolonlar for i in range(satirlar)]

	# Enumerate through the items and fill in the best-value table

	for i, (value, weight) in enumerate(items,1):
		# Increment i, because the first row (0) is the case where no items
		# are chosen, and is already initialized as 0, so we're skipping it

		print('Best values of item%s (Deger:%s, Ağırlık:%s)' % (i, value, weight))
		for capacity in range(kolonlar):
			print('capacity:',capacity)
			# Handle the case where the weight of the current item is greater
			# than the "running capacity" - we can't add it to the knapsack
			if weight > capacity:
				bestvalues[i][capacity] = bestvalues[i - 1][capacity]
			else:
				# Otherwise, we must choose between two possible candidate values:
				# 1) the value of "running capacity" as it stands with the last item
				#    that was computed; if this is larger, then we skip the current item
				# 2) the value of the current item plus the value of a previously computed
				#    set of items, constrained by the amount of capacity that would be left
				#    in the knapsack (running capacity - item's weight)
				candidate1 = bestvalues[i - 1][capacity]
				candidate2 = bestvalues[i - 1][capacity - weight] + value

				# Just take the maximum of the two candidates; by doing this, we are
				# in effect "setting in stone" the best value so far for a particular
				# prefix of the items, and for a particular "prefix" of knapsack capacities
				bestvalues[i][capacity] = max(candidate1, candidate2)

				if candidate2 > candidate1:
					keep[i][capacity] = 1

				print('Best Values')
				print('-----------')
				for sat in bestvalues:print(sat)
				print()
				print('Keep')
				print('-----------')
				for sat in keep: print(sat)

	# Reconstruction
	# Iterate through the values table, and check
	# to see which of the two candidates were chosen. We can do this by simply
	# checking if the value is the same as the value of the previous row. If so, then
	# we say that the item was not included in the knapsack (this is how we arbitrarily
	# break ties) and simply move the pointer to the previous row. Otherwise, we add
	# the item to the reconstruction list and subtract the item's weight from the
	# remaining capacity of the knapsack. Once we reach row 0, we're done
	print('Reconstruction')
	reconstruction = []
	i = len(items)
	j = maxweight
	while i > 0:
		print('item:%s ağırlık:%s: best:%s önceki:%s' % (i,j, bestvalues[i][j], bestvalues[i - 1][j]))
		if bestvalues[i][j] != bestvalues[i - 1][j]:
			reconstruction.append(items[i - 1])
			print('reconstruction:', reconstruction)
			j -= items[i - 1][1]
		i -= 1

	# Reverse the reconstruction list, so that it is presented
	# in the order that it was given
	reconstruction.reverse()

	print()
	print('Secim')
	secim = []
	i = len(items)
	j = maxweight
	while i > 0:
		print('item:%s ağırlık:%s: deger:%s' % (i,j, keep[i][j]))
		if keep[i][j] > 0:
			secim.append(items[i - 1])
			print('secim:', secim)
			j -= items[i - 1][1]
		i -= 1

	# Reverse the reconstruction list, so that it is presented
	# in the order that it was given
	secim.reverse()

	print('Secim:',secim)

	# Return the best value, and the reconstruction list
	return bestvalues[len(items)][maxweight], reconstruction


if __name__ == '__main__':
	filename = "canta_3.txt"
	with open(filename,'r') as f:
		lines = f.readlines()

	maxweight = int(lines[0])
	items = list()
	for line in lines[1:]:
		a = tuple(map(int, line.split()))
		print(a)
		items.append(a)
	# items =[map(int, line.split()) for line in lines[1:]])
	print(items)

	bestvalue, reconstruction = knapsack(items, maxweight)
	print('Best possible value: {0}'.format(bestvalue))
	print('Items:')
	for value, weight in reconstruction:
		print('V: {0}, W: {1}'.format(value, weight))
